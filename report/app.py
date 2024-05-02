from flask import Flask, render_template, jsonify, send_from_directory
import pymysql

app = Flask(__name__)



# 定义处理 /data 路径的视图函数
# @app.route('/data')
@app.route('/api/bar-data')
def data_endpoint():
    db_data = get_db_data()  # 调用 get_db_data() 函数获取数据
    # 使用 jsonify 将数据转换为 JSON 格式并返回
    return jsonify(db_data)
def get_db_data():
    connection = pymysql.connect(host='127.0.0.1', user='root', password='12345678', database='weather')
    cursor = connection.cursor()
    cursor.execute("SELECT date, temp FROM weather.weather_data;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

@app.route('/')
def index():
    data = get_db_data()
    return render_template('index.html', data=data)



# 模拟的天气数据
weather_data = {
    '晴': 150,
    '多云': 120,
    '小雨': 100,
    '阴': 80,
    '雷阵雨': 50,
    '大雨': 30,
    '雾': 20,
    '雪': 10
}

@app.route('/api/weather')
def weather():
    return jsonify(weather_data)



@app.route('/api/pie-data')
def pieWeather():
    return jsonify(weather_data)



# 静态文件路由
@app.route('/bar-chart')
def bar_chart():
    return send_from_directory('static', 'BarChartDisplay.html')

if __name__ == '__main__':
    app.run(debug=True)
