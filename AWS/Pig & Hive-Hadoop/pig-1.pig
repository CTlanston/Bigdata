-- Load daily stock data
daily = LOAD "s3://bigdata-hw6-lanston/pig/NYSE_daily" USING PigStorage('\t') AS AS (
    exchange: chararray, 
    stock: chararray, 
    date: chararray, 
    open_price: float, 
    high_price: float, 
    low_price: float, 
    close_price: float, 
    volume: long, 
    adj_close: float
);

-- Load dividends data
dividends = LOAD "s3://bigdata-hw6-lanston/pig/NYSE_dividends" USING PigStorage('\t')  AS (
    exchange: chararray, 
    stock: chararray, 
    date: chararray, 
    dividend: float
);


-- Join the datasets on stock and date
joinedData = JOIN daily BY (stock, date), dividends BY (stock, date);

-- Calculate dividend/close_price
calculatedData = FOREACH joinedData GENERATE daily::stock AS stock, daily::date AS date, dividends::dividend/daily::close_price AS div_close_ratio;

-- Group all
calculatedData2 = GROUP calculatedData ALL;

-- Calculate the min and max ratios
calculatedData3 = FOREACH calculatedData2 GENERATE 
    MIN(dividend_ratio.ratio) AS min_ratio,
    MAX(dividend_ratio.ratio) AS max_ratio;

-- Join to find the records with min and max ratios
min_record = JOIN joinedData BY ratio, min_max_ratios BY min_ratio;
max_record = JOIN joinedData BY ratio, min_max_ratios BY max_ratio;


-- Prepare the final records for min and max
min_record_final = FOREACH min_record GENERATE 
    FLATTEN(dividend_ratio::stock) AS stock, 
    FLATTEN(dividend_ratio::date) AS date, 
    dividend_ratio::ratio;

max_record_final = FOREACH max_record GENERATE 
    FLATTEN(dividend_ratio::stock) AS stock, 
    FLATTEN(dividend_ratio::date) AS date, 
    dividend_ratio::ratio;

-- Store the final results
STORE min_record_final INTO 's3://bigdata-hw6-lanston/pig/pig_min' USING PigStorage(',');
STORE max_record_final INTO 's3://bigdata-hw6-lanston/pig/pig_max' USING PigStorage(',');




























