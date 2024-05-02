import random
from datetime import datetime, timedelta
import mysql.connector

def generate_weather_data():
    base_date = datetime.now() - timedelta(days=365)
    weather_data = []

    for day in range(365):
        date = base_date + timedelta(days=day)
        weather = {
            'SD': f'{random.randint(50, 90)}%',  # Humidity
            'WD': random.choice(['东风', '西风', '南风', '北风', '东南风', '东北风', '西南风', '西北风']),
            'WS': f'{random.randint(1, 5)}级',  # Wind speed
            'aqi': str(random.randint(20, 150)),
            'aqi_pm25': str(random.randint(20, 150)),
            'city': '101200101',
            'cityname': '武汉',
            'date': date.strftime('%Y-%m-%d'),
            'limitnumber': '单号限行' if day % 2 == 0 else '双号限行',
            'nameen': 'wuhan',
            'njd': f'{random.randint(10, 20)}km',  # Visibility
            'qy': str(random.randint(950, 1050)),
            'rain': f'{random.choice([0, 0, 0, 0, 0, 1, 2])}',  # Random chance of rain
            'rain24h': f'{random.choice([0, 0, 0, 0, 0, 1, 2, 3, 4, 5])}',
            'sd': f'{random.randint(50, 90)}%',
            'temp': f'{random.uniform(15.0, 35.0):.1f}',
            'tempf': f'{(random.uniform(15.0, 35.0) * 9/5 + 32):.1f}',
            'time': f'{random.randint(0, 23):02d}:{random.randint(0, 59):02d}',
            'wde': random.choice(['E', 'W', 'S', 'N', 'SE', 'NE', 'SW', 'NW']),
            'weather': random.choice(['晴', '阴', '多云', '小雨', '中雨']),
            'weathercode': random.choice(['d00', 'd02', 'd03', 'd04', 'd05']),
            'weathere': random.choice(['Clear', 'Overcast', 'Cloudy', 'Light Rain', 'Moderate Rain']),
            'wse': f'{random.randint(1, 10)}km/h'
        }
        weather_data.append(weather)

    return weather_data


def insert_weather_data(weather_data):
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='weather'
    )
    cursor = db_connection.cursor()

    insert_query = """
    INSERT INTO weather_data (
    nameen, cityname, city, temp, tempf, WD, wde, WS, wse, SD, sd_1, qy, njd, time,
    rain, rain24h, aqi, aqi_pm25, weather, weathere, weathercode, limitnumber, date
    ) VALUES (
    %(nameen)s, %(cityname)s, %(city)s, %(temp)s, %(tempf)s, %(WD)s, %(wde)s, %(WS)s, 
    %(wse)s, %(SD)s, %(sd)s, %(qy)s, %(njd)s, %(time)s, %(rain)s, %(rain24h)s, 
    %(aqi)s, %(aqi_pm25)s, %(weather)s, %(weathere)s, %(weathercode)s, %(limitnumber)s, %(date)s
    )
    """

    # Insert each item into the database
    for data in weather_data:
        cursor.execute(insert_query, data)

    db_connection.commit()
    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    # Example of how to use the function
    weather_data = generate_weather_data()
    insert_weather_data(weather_data)