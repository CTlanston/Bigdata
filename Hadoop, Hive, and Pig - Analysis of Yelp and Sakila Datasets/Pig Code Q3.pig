-- Enter Pig (grunt)
pig
-- Load the data
retail = LOAD 's3://datasets-achumac/Online Retail/online-retail-dataset.csv' USING PigStorage(',') AS (InvoiceNo:
int, StockCode: chararray, Description: chararray, Quantity: int, InvoiceDate: chararray, UnitPrice: double,
CustomerID: int, Country: chararray);
-- Filter the sales
filtered = FILTER retail BY UnitPrice>5 AND Quantity<10;
-- Group
retail_groupped = GROUP filtered ALL;
-- Count
count = FOREACH retail_groupped GENERATE COUNT(filtered.InvoiceNo);
-- dump count;
