import mysql.connector
from scrapy.exceptions import DropItem


class MySQLStorePipeline(object):
    def open_spider(self, spider):
        # Initialize database connection and store it in an instance variable
        self.conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1',
                                            database='weather')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # Close the database connection
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""
                INSERT INTO weather_data (nameen, cityname, city, temp, tempf, WD, wde, WS, wse, SD, sd_1, qy, njd, time, rain, rain24h, aqi, aqi_pm25, weather, weathere, weathercode, limitnumber, date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                item.get('nameen'), item.get('cityname'), item.get('city'), item.get('temp'), item.get('tempf'),
                item.get('WD'), item.get('wde'), item.get('WS'), item.get('wse'), item.get('SD'), item.get('sd'),
                item.get('qy'), item.get('njd'), item.get('time'), item.get('rain'), item.get('rain24h'),
                item.get('aqi'), item.get('aqi_pm25'), item.get('weather'), item.get('weathere'),
                item.get('weathercode'),
                item.get('limitnumber'), item.get('date')
            ))
            self.conn.commit()
            spider.logger.info("Item stored in MySQL")
            print("Item stored in MySQL-------------------------")
        except mysql.connector.Error as e:
            spider.logger.error(f"Error inserting item into MySQL: {e}")
            raise DropItem(f"Error inserting item: {e}")

        return item
