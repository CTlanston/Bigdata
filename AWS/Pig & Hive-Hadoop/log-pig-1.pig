loglines = LOAD 's3://bigdata-hw6-lanston/access_log_Jul95.txt' USING TextLoader AS (line:chararray);



logs = FOREACH loglines GENERATE FLATTEN(
    REGEX_EXTRACT_ALL(
        line,
        '^(\\S+) - - \\[(.*?)\\] "(\\S+ \\S+ \\S+)" (\\d{3}) (\\d+|-) "(.*?)" "(.*?)"'
    )
) AS (ip:chararray, timestamp:chararray, request:chararray, status:int, bytes:long, referrer:chararray, useragent:chararray);


STORE logs INTO 'hdfs:///hive/warehouse/tripadvisor' USING PigStorage(',');
