
create database if not exists weather;
use weather;
CREATE TABLE if not exists weather_data (
    nameen VARCHAR(255) COMMENT '英文名称',
    cityname VARCHAR(255) COMMENT '中文名称',
    city VARCHAR(50) COMMENT '城市代码',
    temp FLOAT COMMENT '温度',
    tempf FLOAT COMMENT '华氏温度',
    WD VARCHAR(50) COMMENT '风向',
    wde VARCHAR(50) COMMENT '风向英文缩写',
    WS VARCHAR(50) COMMENT '风力等级',
    wse VARCHAR(50) COMMENT '风速',
    SD VARCHAR(50) COMMENT '相对湿度',
    sd_1 VARCHAR(50) COMMENT '相对湿度百分比',
    qy INT COMMENT '气压',
    njd VARCHAR(50) COMMENT '能见度',
    time TIME COMMENT '时间',
    rain FLOAT COMMENT '当前降雨量',
    rain24h FLOAT COMMENT '24小时降雨量',
    aqi INT COMMENT '空气质量指数',
    aqi_pm25 INT COMMENT 'PM2.5指数',
    weather VARCHAR(100) COMMENT '天气状况',
    weathere VARCHAR(100) COMMENT '天气状况英文',
    weathercode VARCHAR(50) COMMENT '天气状况代码',
    limitnumber VARCHAR(50) COMMENT '限行规则',
    `date` DATE COMMENT '日期'
);



CREATE TABLE weather_data_history (
    ctnb STRING COMMENT '城市编号',          -- 城市编号
    prvn STRING COMMENT '所属省份',          -- 所属省份
    pftn STRING COMMENT '所属地级市',        -- 所属地级市
    ctn STRING COMMENT '城市名称',           -- 城市名称
    `date` STRING COMMENT '日期',             -- 日期
    dywek STRING COMMENT '星期时间',         -- 星期时间
    htmpt STRING COMMENT '最高气温',         -- 最高气温，单位：℃
    ltmpt STRING COMMENT '最低气温',         -- 最低气温，单位：℃
    wthcdt STRING COMMENT '天气情况',        -- 天气情况
    wnddrt STRING COMMENT '风向',           -- 风向
    wndfrc STRING COMMENT '风力'            -- 风力
) COMMENT '地理位置维度表，包含城市及其所在省份和地级市的信息';

