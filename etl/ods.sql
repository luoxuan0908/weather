
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



-- auto-generated definition
create temporary table weather_data
(
    nameen      string comment '英文名称',
    cityname    string comment '中文名称',
    city        string comment '城市代码',
    temp        float comment '温度',
    tempf       float comment '华氏温度',
    wd          string comment '风向',
    wde         string comment '风向英文缩写',
    ws          string comment '风力等级',
    wse         string comment '风速',
    sd          string comment '相对湿度',
    sd_1        string comment '相对湿度百分比',
    qy          int comment '气压',
    njd         string comment '能见度',
    `time`      string comment '时间',
    rain        float comment '当前降雨量',
    rain24h     float comment '24小时降雨量',
    aqi         int comment '空气质量指数',
    aqi_pm25    int comment 'PM2.5指数',
    weather     string comment '天气状况',
    weathere    string comment '天气状况英文',
    weathercode string comment '天气状况代码',
    limitnumber string comment '限行规则',
    `date`      string comment '日期'
);

alter table weather_data
    set tblproperties ('comment' = 'Weather data table');

