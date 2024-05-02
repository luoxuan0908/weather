import scrapy

class WeatherItem(scrapy.Item):
    nameen = scrapy.Field()  # 英文名称
    cityname = scrapy.Field()  # 中文名称
    city = scrapy.Field()  # 城市代码
    temp = scrapy.Field()  # 温度
    tempf = scrapy.Field()  # 华氏温度
    WD = scrapy.Field()  # 风向
    wde = scrapy.Field()  # 风向英文缩写
    WS = scrapy.Field()  # 风力等级
    wse = scrapy.Field()  # 风速
    SD = scrapy.Field()  # 相对湿度，注意json中的键名是'S67%'，这里假设是'S'，你可能需要根据实际情况调整
    sd = scrapy.Field()  # 相对湿度百分比
    qy = scrapy.Field()  # 气压
    njd = scrapy.Field()  # 能见度
    time = scrapy.Field()  # 时间
    rain = scrapy.Field()  # 当前降雨量
    rain24h = scrapy.Field()  # 24小时降雨量
    aqi = scrapy.Field()  # 空气质量指数
    aqi_pm25 = scrapy.Field()  # PM2.5指数
    weather = scrapy.Field()  # 天气状况
    weathere = scrapy.Field()  # 天气状况英文
    weathercode = scrapy.Field()  # 天气状况代码
    limitnumber = scrapy.Field()  # 限行规则
    date = scrapy.Field()  # 日期
    pass