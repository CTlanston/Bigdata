-- Creating database to store data
CREATE DATABASE retail;
-- Column definitions (refer to data for column names and data types)
CREATE TABLE online_retail
(InvoiceNo INT,
StockCode STRING,
Description STRING,
Quantity INT,
InvoiceDate TIMESTAMP,
UnitPrice DOUBLE,
CustomerID INT,
Country STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
-- Load data
LOAD DATA INPATH 's3://datasets-achumac/Online Retail/online-retail-dataset.csv' OVERWRITE INTO TABLE
online_retail;
-- Query: execute a query to identify the number of orders with UnitPrice>5 and Quantity<10
SELECT count(*) FROM online_retail where UnitPrice>5 and Quantity<10;
