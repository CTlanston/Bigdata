-- Create three happiness tables (happy1, happy2, and happy3) in Hive
-- on Hive
create database happiness;
-- based on 2016
create table happiness.happy1 (Country varchar(30), Region varchar(50), `Happiness_Rank`
int, `Happiness Score` double, `Lower Confidence Interval` double, `Upper Confidence Interval`
double, `Economy (GDP per Capita)` double, Family double, `Health (Life Expectancy)` double,
Freedom double, `Trust (Government Corruption)` double, Generosity double, `Dystopia
Residual` double) row format delimited fields terminated by ',' lines terminated by '\n';
create table happiness.happy2 (Country varchar(30), Region varchar(50), `Happiness_Rank`
int, `Happiness Score` double, `Lower Confidence Interval` double, `Upper Confidence Interval`
double, `Economy (GDP per Capita)` double, Family double, `Health (Life Expectancy)` double,
Freedom double, `Trust (Government Corruption)` double, Generosity double, `Dystopia
Residual` double) row format delimited fields terminated by ',' lines terminated by '\n';
create table happiness.happy3 (Country varchar(30), Region varchar(50), `Happiness_Rank`
int, `Happiness Score` double, `Lower Confidence Interval` double, `Upper Confidence Interval`
double, `Economy (GDP per Capita)` double, Family double, `Health (Life Expectancy)` double,
Freedom double, `Trust (Government Corruption)` double, Generosity double, `Dystopia
Residual` double) row format delimited fields terminated by ',' lines terminated by '\n';
-- Load csv file in RDS mySQL (data1)
create schema happiness;
create table happiness.data1(
Country varchar(30), Region varchar(50), `Happiness_Rank` int, `Happiness Score` double,
`Lower Confidence Interval` double, `Upper Confidence Interval` double, `Economy (GDP per
Capita)` double, Family double, `Health (Life Expectancy)` double, Freedom double, `Trust
(Government Corruption)` double, Generosity double, `Dystopia Residual` double);
LOAD DATA LOCAL
INFILE '/Users/FrancisJingo1/Downloads/worldhappiness/2016.csv'
INTO TABLE happiness.data1
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '\b'
LINES TERMINATED BY '\n' IGNORE 1 ROWS;
-- Using Sqoop import happiness data (data1) from RDS to S3
sqoop import --connect
jdbc:mysql://mysql-rds-lab5.c8sutaslqpmn.us-east-1.rds.amazonaws.com/happiness
--username admin --password admin1234 --delete-target-dir --target-dir
s3://group-assignment-2/data1/ --query 'select * from data1 where $CONDITIONS' --split-by
data1.Happiness_Rank;
-- On Hive
-- and then use HiveQL to import that S3 data in Hive (happy1)
LOAD DATA INPATH 's3://group-assignment-2/data1/' INTO TABLE happiness.happy1;
-- Using Sqoop, import happiness data (data1) from RDS to Hive (happy2)
sqoop import --connect
jdbc:mysql://mysql-rds-lab5.c8sutaslqpmn.us-east-1.rds.amazonaws.com/happiness
--username admin --password admin1234 --query 'select * from data1 where $CONDITIONS'
--split-by data1.Happiness_Rank --fields-terminated-by ',' --hive-import --hive-database
happiness --hive-table happy2 --delete-target-dir --target-dir
/user/hive/warehouse/happiness.db/happy2;
-- Using HiveQL, import S3 data (data2) in Hive (happy3).
LOAD DATA INPATH 's3://group-assignment-2/data2/2016.csv' INTO TABLE happiness.happy3;
ALTER TABLE happiness.happy3 SET TBLPROPERTIES ("skip.header.line.count"="1");
