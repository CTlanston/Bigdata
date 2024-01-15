-- Create an external table nyTaxi
CREATE EXTERNAL TABLE nyTaxi (
    VendorID INT,
    lpep_pickup_datetime STRING,
    lpep_dropoff_datetime STRING,
    store_and_fwd_flag STRING,
    RatecodeID INT,
    PULocationID INT,
    DOLocationID INT,
    passenger_count INT,
    trip_distance FLOAT,
    fare_amount FLOAT,
    extra FLOAT,
    mta_tax FLOAT,
    tip_amount FLOAT,
    tolls_amount FLOAT,
    ehail_fee STRING,
    improvement_surcharge FLOAT,
    total_amount FLOAT,
    payment_type INT,
    trip_type INT
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
STORED AS TEXTFILE 
LOCATION 's3://bigdata-hw6-lanston/hive/';

-- Get distinct RatecodeID from the table
SELECT DISTINCT RatecodeID FROM nyTaxi;

-- Show all rows/columns where RatecodeID = 1
SELECT * FROM nyTaxi WHERE RatecodeID = 1;



-- start hive: hive 
-- end hive: 
Run the entire script using hive -f nytaxi.hql.
Or, input each command in the Hive shell sequentially.