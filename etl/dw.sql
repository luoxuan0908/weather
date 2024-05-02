-- 时间维度表
CREATE TABLE dim_date (
    date_key STRING COMMENT '日期ID，格式为YYYYMMDD',
    year_val INT COMMENT '年份',
    month_val INT COMMENT '月份',
    day_val INT COMMENT '日期',
    quarter_val INT COMMENT '季度',
    week_num INT COMMENT '一年中的第几周'
)
COMMENT '时间维度表，包含日期的详细分解'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;



-- 地理维度表

CREATE TABLE dim_geography (
    city_id INT COMMENT '城市编号，提供唯一的城市标识',
    province STRING COMMENT '城市所属的省份',
    prefecture STRING COMMENT '城市所属的地级市',
    city_name STRING COMMENT '城市名称'
)
COMMENT '地理位置维度表，包含城市及其所在省份和地级市的信息';
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- 从历史数据表中导入地理位置维度表
INSERT INTO dim_geography -- (city_id, province, prefecture, city_name)
SELECT
    ctnb as city_id,
    prvn as province,
    pftn as prefecture,
    ctn as city_name
FROM weather.weather_data_history
GROUP BY ctnb, prvn, pftn, ctn;



drop table  if exists weather.fact_weather;
CREATE TABLE if not exists weather.fact_weather (
    ctnb STRING COMMENT '城市编号',
    prvn STRING COMMENT '所属省份',
    pftn STRING COMMENT '所属地级市',
    ctn STRING COMMENT '城市名称',
    region STRING COMMENT '区域分类（南方、北方）',
    day_of_date STRING COMMENT '日期',
    day_of_year INT COMMENT '年份',
    day_of_month INT COMMENT '月份',
    day_of_quarter INT COMMENT '季度',
    day_of_week STRING COMMENT '星期几',
    max_temperature DOUBLE COMMENT '最高气温',
    min_temperature DOUBLE COMMENT '最低气温',
    temperature_range DOUBLE  COMMENT '气温范围，计算列',
    weather_condition_code STRING COMMENT '天气情况编码',
    wind_direction STRING COMMENT '风向',
    wind_force STRING COMMENT '风力',
    weather_warning STRING COMMENT '天气预警类型（高温预警、低温预警、大风预警）'
) COMMENT '包含地理位置、日期维度以及天气详细情况的事实表'
PARTITIONED BY (ds string);

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












