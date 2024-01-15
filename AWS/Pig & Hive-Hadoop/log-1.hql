CREATE EXTERNAL TABLE  tripadvisor_logs (
    `ip` STRING,
    `timestamp` STRING,
    `request` STRING,
    `status` INT,
    `bytes` BIGINT,
    `referrer` STRING,
    `useragent` STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION 'hdfs:///hive/warehouse/tripadvisor';


SELECT ip, COUNT(*) AS error_count
FROM tripadvisor_logs 
WHERE status = 404
GROUP BY ip;