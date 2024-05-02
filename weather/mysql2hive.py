import mysql.connector

def fetch_data_from_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='weather'
    )
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to fetch data as dictionaries
    query = "SELECT * FROM weather_data;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


from pyhive import hive


def generate_insert_query(data_sample, table_name, partition_column):
    if not data_sample:
        return None
    # 获取所有字段名，不包含分区列，因为它将在运行时指定
    non_partition_columns = list(data_sample.keys())

    # 构建基本的SQL插入语句
    base_query = f"INSERT INTO TABLE {table_name} "
    # 列出所有非分区列
    base_query += " (" + ', '.join([f"`{col.lower()}`" for col in non_partition_columns]) + ")"
    # 对于每个列添加占位符
    base_query += " VALUES (" + ', '.join(['%s' for _ in non_partition_columns]) + ")"
    return base_query



def write_data_to_hive(data):
    if not data:
        print("No data to write to Hive.")
        return

    conn = hive.Connection(host='101.126.4.10', port=10000, username='hive', database='weather', auth='CUSTOM', password="hive")
    cursor = conn.cursor()



    # 生成插入语句
    insert_query = generate_insert_query(data[0], "weather_data", "ds")
    print(insert_query)
    # 执行插入操作
    for row in data:
        # 根据字段顺序整理数据，确保包含分区值
        values = tuple(row[col] for col in row if col != 'ds')
        cursor.execute(insert_query, values)

    conn.commit()
    cursor.close()
    conn.close()


def main():
    data = fetch_data_from_mysql()
    if data:
        write_data_to_hive(data)
    else:
        print("No data found to transfer.")

if __name__ == "__main__":
    main()