vi log.sh
pig logs.pig
hive -f logs.hql
:wq

vi logs.pig
loglines = LOAD 's3://bigdata-hw6-lanston/access_log_Jul95.txt' USING TextLoader AS (line:chararray);

logs = FOREACH loglines GENERATE FLATTEN(
    REGEX_EXTRACT_ALL(
        line,
        '^(\\S+) - - \\[(.*?)\\] "(\\S+ \\S+ \\S+)" (\\d{3}) (\\d+|-) "(.*?)" "(.*?)"'
    )
) AS (ip:chararray, timestamp:chararray, request:chararray, status:int, bytes:long, referrer:chararray, useragent:chararray);


STORE logs INTO 'hdfs:///hive/warehouse/tripadvisor' USING PigStorage(',');

:wq


vi logs.hql

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

:wq

bash log.sh
