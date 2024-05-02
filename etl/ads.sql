## 每日城市气温报告

```SQL

drop table  if exists weather.ads_daily_city_temperature_report;
CREATE TABLE if not exists weather.ads_daily_city_temperature_report (
    city_name STRING COMMENT '城市名称',
    report_date STRING COMMENT '报告日期',
    max_temperature DOUBLE COMMENT '最高气温',
    min_temperature DOUBLE COMMENT '最低气温',
    temperature_range DOUBLE COMMENT '气温范围',
    create_dt TIMESTAMP COMMENT '记录创建时间',
    update_dt TIMESTAMP COMMENT '记录更新时间'
)COMMENT '存储每日城市气温报告'
PARTITIONED BY (ds STRING)
;



INSERT INTO weather.ads_daily_city_temperature_report partition (ds = '20240428')
SELECT
    ctn AS city_name,
    day_of_date AS report_date,
    max_temperature,
    min_temperature,
    temperature_range,
    current_timestamp() AS create_dt,
    current_timestamp() AS update_dt
FROM
    weather.fact_weather
WHERE
    ds = '2024-04-28' and day_of_year ='2022'

```




## 城市月平均气温

```SQL


drop table if exists weather.ads_city_monthly_avg_temp;
CREATE TABLE if not exists weather.ads_city_monthly_avg_temp
(
    prvn               STRING COMMENT '省份',
    pftn               STRING COMMENT '地级市',
    day_of_month       INT COMMENT '月份',
    avg_max_temp       DOUBLE COMMENT '平均最高气温',
    avg_min_temp       DOUBLE COMMENT '平均最低气温',
    created_at         TIMESTAMP COMMENT '创建时间',
    updated_at         TIMESTAMP COMMENT '更新时间'
) COMMENT '城市月平均气温'
PARTITIONED BY (ds string);


INSERT overwrite table weather.ads_city_monthly_avg_temp partition (ds='20240430')
SELECT
    prvn,
    pftn,
    day_of_month,
    AVG(max_temperature) AS avg_max_temp,
    AVG(min_temperature) AS avg_min_temp,
    CURRENT_TIMESTAMP AS created_at,
    CURRENT_TIMESTAMP AS updated_at
FROM
    weather.fact_weather
GROUP BY
    prvn, pftn, day_of_month;


    mysql 表
    drop table if exists weather.ads_city_monthly_avg_temp;
CREATE TABLE if not exists weather.ads_city_monthly_avg_temp
(
    prvn               VARCHAR(255) COMMENT '省份',
    pftn               VARCHAR(255) COMMENT '地级市',
    day_of_month       INT COMMENT '月份',
    avg_max_temp       DOUBLE COMMENT '平均最高气温',
    avg_min_temp       DOUBLE COMMENT '平均最低气温',
    created_at         TIMESTAMP COMMENT '创建时间',
    updated_at         TIMESTAMP COMMENT '更新时间'
) COMMENT '城市月平均气温';
```




## 城市最高最低温度记录

```SQL
-- 创建新表来存储城市的最高和最低温度记录，包括时间戳和分区字段
CREATE TABLE IF NOT EXISTS weather.ads_city_temperature_records
(
    prvn           string COMMENT '省份',
    pftn           string COMMENT '地级市',
    record_high    DOUBLE COMMENT '最高温度记录',
    record_low     DOUBLE COMMENT '最低温度记录',
    created_at     date COMMENT '记录创建时间',
    updated_at     date  COMMENT '记录更新时间'
) comment '城市最高最低温度记录'
    partitioned by (ds string)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '&';

-- 插入数据到新表中
INSERT OVERWRITE TABLE weather.ads_city_temperature_records PARTITION (ds='20240428')
SELECT
    prvn,
    pftn,
    MAX(max_temperature) AS record_high,
    MIN(min_temperature) AS record_low,
    CURRENT_TIMESTAMP AS created_at,
    CURRENT_TIMESTAMP AS updated_at
FROM    weather.fact_weather
GROUP BY prvn, pftn;
```






## 区域季节气温分析

```SQL
drop table if exists weather.ads_region_seasonal_temp;
CREATE TABLE IF NOT EXISTS weather.ads_region_seasonal_temp (
    region STRING COMMENT '地区',
    season STRING COMMENT '季节',
    avg_max_temp double COMMENT '平均最高气温',
    avg_min_temp double COMMENT '平均最低气温',
    created_at     date COMMENT '记录创建时间',
    updated_at     date  COMMENT '记录更新时间'
)
COMMENT '区域季节气温分析表'
PARTITIONED BY (
    ds STRING COMMENT '分区开始日期'
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '&';

INSERT OVERWRITE TABLE weather.ads_region_seasonal_temp PARTITION (ds='20240428')
SELECT
    region,
    season,
    AVG(max_temperature) AS avg_max_temp,
    AVG(min_temperature) AS avg_min_temp,
    CURRENT_TIMESTAMP AS created_at,
    CURRENT_TIMESTAMP AS updated_at
FROM fact_weather
GROUP BY region, season;
```






## 城市年度天气报告表

```SQL
drop table if exists weather.ads_city_annual_weather_summary;
CREATE TABLE if not exists weather.ads_city_annual_weather_summary (
    day_of_year INT COMMENT '年份',
    province string COMMENT '省份',
    city string COMMENT '城市',
    ctn string COMMENT '城市名称',
    weather_condition_code VARCHAR(50) COMMENT '天气状况代码',
    total bigint COMMENT '该天气状况总次数',
    created_at     date COMMENT '记录创建时间',
    updated_at     date  COMMENT '记录更新时间'
)
COMMENT '城市年度天气报告表'
PARTITIONED BY (ds string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '&';
```


