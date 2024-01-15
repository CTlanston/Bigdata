from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = spark.read.load("s3://lanston-bigdata-lab6/lab6/data.csv", format="csv", sep="", inferSchema="true", header="true")

df.write.option("path", "/user/hadoop/nasa")  # save it as csv

df.write.format("parquet").option("path", "/user/hadoop/lab6_parquet").save()

# read it as parquet
parquet_path = "/user/hadoop/lab6_parquet"
df_parquet = spark.read.parquet(parquet_path)

df.createOrReplaceTempView("web_logs")

import time

start_time = time.time()
top_hosts_by_url_count = spark.sql("""
SELECT host, COUNT(url) as cnt 
FROM web_logs
GROUP BY host
ORDER BY cnt DESC
LIMIT 5
""")
csv_query_1_time = time.time() - start_time

start_time = time.time()
top_hosts_by_bytes = spark.sql("""
SELECT host, SUM(bytes) as byte
FROM web_logs
GROUP BY host
ORDER BY byte DESC
LIMIT 5
""")
csv_query_2_time = time.time() - start_time

start_time = time.time()
top_urls_by_count = spark.sql("""
SELECT url, COUNT(*) as cnt
FROM web_logs
GROUP BY url
ORDER BY cnt DESC
LIMIT 5
""")
csv_query_3_time = time.time() - start_time

start_time = time.time()
top_urls_by_bytes = spark.sql("""
SELECT url, SUM(bytes) as byte
FROM web_logs
GROUP BY url
ORDER BY byte DESC
LIMIT 5
""")
csv_query_4_time = time.time() - start_time

df_parquet.createOrReplaceTempView("web_logs_par")

start_time = time.time()
df1 = spark.sql("""
SELECT host, COUNT(url) as cnt 
FROM web_logs_par 
GROUP BY host
ORDER BY cnt DESC 
LIMIT 5
""")
df1.show()
print("Query 1 Time:", time.time() - start_time)
par_query_1_time = time.time() - start_time

start_time = time.time()
df2 = spark.sql("""
SELECT host, SUM(bytes) as byte 
FROM web_logs_par 
GROUP BY host
ORDER BY byte DESC 
LIMIT 5
""")
df2.show()
print("Query 2 Time:", time.time() - start_time)
par_query_2_time = time.time() - start_time

start_time = time.time()
df3 = spark.sql("""
SELECT url, COUNT(*) as cnt 
FROM web_logs_par 
GROUP BY url
ORDER BY cnt DESC 
LIMIT 5
""")
df3.show()
print("Query 3 Time:", time.time() - start_time)
par_query_3_time = time.time() - start_time

start_time = time.time()
df4 = spark.sql("""
SELECT url, SUM(bytes) as byte 
FROM web_logs_par 
GROUP BY url
ORDER BY byte DESC 
LIMIT 5
""")
df4.show()
print("Query 4 Time:", time.time() - start_time)
par_query_4_time = time.time() - start_time

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Initialize Spark session
spark = SparkSession.builder.appName("Query Time Comparison").getOrCreate()

# Data
data = [
    ("Query 1", csv_query_1_time, par_query_1_time),
("Query 2", csv_query_2_time, par_query_2_time),
("Query 3", csv_query_3_time, par_query_3_time),
("Query 4", csv_query_4_time, par_query_4_time)
]

Define schema
schema = StructType([
StructField("Query", StringType(), True),
StructField("CSV Query Time (s)", FloatType(), True),
StructField("Parquet Query Time (s)", FloatType(), True)
])

Create DataFrame
df = spark.createDataFrame(data, schema)

Display DataFrame
df.show()
