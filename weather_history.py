import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

def connect_to_db(host, user, password, database):
    """连接到MySQL数据库"""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

def write_to_db(connection, data, table_name):
    """将数据写入数据库"""
    cursor = connection.cursor()
    # 替换NaN值为None或其他合适的默认值
    data = data.where(pd.notnull(data), None)
    placeholders = ", ".join(["%s"] * len(data.columns))
    columns = ", ".join(data.columns)
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    for _, row in data.iterrows():
        try:
            cursor.execute(sql, tuple(row))
            connection.commit()
        except mysql.connector.Error as e:
            print(f"Failed to insert row: {e}")
            continue
    print(f"Inserted rows into {table_name}")


def read_and_process_files(root_dir, table_name, db_config):
    """读取所有.xlsx文件并写入数据库"""
    connection = connect_to_db(**db_config)
    if connection:
        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                print(f"Processing file: {file}")
                if file.endswith('.xlsx'):
                    file_path = os.path.join(subdir, file)
                    print(f"Processing file: {file_path}")
                    # 跳过前两行，并设置列名
                    data = pd.read_excel(file_path, skiprows=2)
                    data.columns = ['ctnb', 'prvn', 'pftn', 'ctn', 'date', 'dywek', 'htmpt', 'ltmpt', 'wthcdt', 'wnddrt', 'wndfrc']
                    write_to_db(connection, data, table_name)
        connection.close()

if __name__ == "__main__":
    root_dir = '/Users/luoxuan/云原生/CEDS_天气 2011-2022'
    table_name = 'weather_data_history'
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '12345678',
        'database': 'weather'
    }
    read_and_process_files(root_dir, table_name, db_config)



