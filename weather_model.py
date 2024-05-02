import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



# 使用read_excel来读取Excel文件
data = pd.read_excel('weather_fact_weather_2.xlsx', engine='openpyxl')

# 查看数据的前几行
print(data.head())

# 确保年份是整数型，气温是浮点型

data['Date'] = pd.to_datetime(data['day_of_date'])
# 从日期中提取年份
data['Year'] = data['day_of_year'].astype(int)

data['Average_Temperature'] = data['max_temperature'].astype(float)


print(data[['Date', 'Year', 'Average_Temperature']])
# data['Average_Temperature'] = data['Average_Temperature'].astype(float)





plt.figure(figsize=(10, 5))
plt.scatter(data['Year'], data['Average_Temperature'], color='blue')
plt.title('Average Temperature Over Years')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.grid(True)
plt.show()



# 将年份数据转换为2D数组，因为scikit-learn需要这种格式
X = data['Year'].values.reshape(-1, 1)
y = data['Average_Temperature'].values

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 获取回归系数和截距
slope = model.coef_[0]
intercept = model.intercept_
print(f"The slope is {slope} and the intercept is {intercept}")



# 预测
y_pred = model.predict(X)

# 可视化实际值与预测值
# 创建一个图形的框架，设置图的大小为宽10英寸，高5英寸
plt.figure(figsize=(10, 5))
# 绘制散点图，x轴是年份，y轴是平均气温，点的颜色为蓝色，标签名为“实际”
plt.scatter(data['Year'], data['Average_Temperature'], color='blue', label='Actual')
# 绘制预测的线性回归线，x轴是年份，y轴是模型预测的气温，线的颜色为红色，线宽为2，标签名为“拟合”
plt.plot(data['Year'], y_pred, color='red', linewidth=2, label='Fit')
# 设置图的标题为“年度气温线性拟合”
plt.title('Linear Fit of Temperature over Years')
# 设置x轴的标签为“年份”
plt.xlabel('Year')
# 设置y轴的标签为“平均气温”
plt.ylabel('Average Temperature')
# 显示图例，图例会展示“实际”和“拟合”的标签说明
plt.legend()
# 显示网格
plt.grid(True)

# 显示整个图形
plt.show()



#
# 我们可以看到有两种不同的标记：蓝色的点和一条红色的线。
#
# 蓝色的点：每个点代表在特定年份测量的平均气温。点的位置告诉我们在那一年里，气温是多少。
# 红色的线：这条线代表线性回归模型的预测结果。它是通过分析所有蓝色点的分布来得出的，试图找到一个最佳的直线来代表这些点的整体趋势。
# 从图中可以看出，蓝色的点围绕一条直线分布，但是点的上下波动相当大。这说明虽然我们可以用一条直线大概概括气温随年份的变化趋势，实际的气温数据却在每年都有很大的变动，这些变动没有被直线捕捉到。
#
# 红色的线是平直的，这意味着模型预测气温随时间的变化是恒定的，而不考虑实际上每年的波动。所以，这个线性模型可能过于简化了实际的情况。
#
# 如果我们想要更准确地预测每年的气温，可能需要一个更复杂的模型来捕捉气温随时间变化的所有细节。此外，气温数据可能受到多种因素的影响，比如季节变化、地理位置、大气条件等，这些都需要考虑进去才能做出更准确的预测。