import scrapy
import json

from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    # 目标URL
    start_urls = ['http://d1.weather.com.cn/sk_2d/101200101.html']
    # 定义HTTP请求头
    custom_headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'f_city=%E6%AD%A5%E6%B1%89%7C101200101%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1713442259,1713445506; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1713445689',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.weather.com.cn/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        # 输出原始响应内容以供检查
        print(f"Response Body:\n{response.body.decode('utf-8')}")
        import re
        json_data = re.search(r'\{.*\}', response.text).group(0)
        json_response = json.loads(json_data)
        print(json_response)
        # 假设response.json()返回了JSON响应数据
        # json_response = response.json()

        # 创建WeatherItem实例并填充数据
        weather_item = WeatherItem()
        # 遍历json_response中的所有项，并填充到weather_item中
        for key, value in json_response.items():
            # 检查WeatherItem是否有对应的字段
            if key in weather_item.fields:
                weather_item[key] = value

        # 返回填充好的weather_item
        yield weather_item



if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute('scrapy crawl weather'.split())
