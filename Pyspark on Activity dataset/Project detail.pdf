from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, IntegerType, LongType
from pyspark.sql.functions import window, mean, count, col, when, sum as sum_, lag, sqrt
import matplotlib.pyplot as plt
import time

# Initialize Spark Session
spark = SparkSession.builder.appName("ActivityRecommendation").getOrCreate()

# Define the schema for the data
schema = StructType([
    StructField("Arrival_Time", LongType(), True),
    StructField("Creation_Time", LongType(), True),
    StructField("Device", StringType(), True),
    StructField("gt", StringType(), True),
    StructField("x", DoubleType(), True),
    StructField("y", DoubleType(), True),
    StructField("z", DoubleType(), True)
])

# Reading data as streaming
input_path = "/*.json"
streaming_df = spark.readStream.schema(schema).option("maxFilesPerTrigger", 5).json(input_path)
withEventTime = streaming_df.withColumn("event_time", (col("Creation_Time") / 1e9).cast("timestamp"))

# Processing streaming data for various window sizes
window_sizes = ["5 minutes", "15 minutes", "30 minutes"]
queries = []
processing_times = {}

for window_size in window_sizes:
    query_name = window_size.replace(" ", "_") + "_window_query"
    for query in spark.streams.active:
        if query.name == query_name:
            query.stop()

    grouped_df = withEventTime.groupBy(window(col("event_time"), window_size), "gt").agg(
        count("gt").alias("count_gt"),
        mean("x").alias("mean_x"),
        mean("y").alias("mean_y"),
        mean("z").alias("mean_z")
    )

    start_time = time.time()
    query = grouped_df.writeStream.queryName(query_name).format("memory").outputMode("complete").start()
    queries.append((query, start_time))

time.sleep(60)  # Allow processing time

for query, start_time in queries:
    if query.isActive:
        query_name = query.name
        print(f"Showing results for: {query_name}")
        spark.sql(f"SELECT * FROM {query_name}").show()
        end_time = time.time()
        print(f"Processing time for {query_name}: {end_time - start_time} seconds")
        query.stop()

# Visualizing the processing times
window_sizes = [ws.replace("_", " ") for ws in processing_times.keys()]
times = list(processing_times.values())

plt.figure(figsize=(10, 6))
plt.bar(window_sizes, times, color='blue')
plt.xlabel('Window Sizes')
plt.ylabel('Processing Time (seconds)')
plt.title('Processing Times for Different Window Sizes')
plt.xticks(rotation=45)

for i, time in enumerate(times):
    plt.text(i, time + 0.5, f'{time:.2f}', ha='center')

plt.show()

# Part 2: Calculating Standing Recommendations



### Calculate "Standing Recommended"

# Filtering and creating columns for 'sit' and 'stand' counts
transformed_df = (withEventTime
                  .filter(col("gt").isin("sit", "stand"))
                  .withColumn("sit_count", when(col("gt") == "sit", 1).otherwise(0))
                  .withColumn("stand_count", when(col("gt") == "stand", 1).otherwise(0)))

# Grouping by time window and aggregating counts
windowed_counts = (transformed_df
                   .groupBy(window(col("event_time"), "15 minutes"))
                   .agg(sum_("sit_count").alias("total_sit"),
                        sum_("stand_count").alias("total_stand")))

# Determining the recommendation based on counts
recommendation_df = windowed_counts.withColumn("recommendation", 
                                               when(col("total_sit") > col("total_stand"), "standing recommended")
                                               .otherwise(None))

###: Calculate "Move Recommended"

# Grouping by time window and calculating mean positions
mean_positions_df = (withEventTime
                     .groupBy(window(col("event_time"), "15 minutes"))
                     .agg(mean("x").alias("mean_x"),
                          mean("y").alias("mean_y"),
                          mean("z").alias("mean_z")))

# Creating a window for calculations
w = Window.orderBy("window")

# Calculating distance and previous distance
distance_df = (mean_positions_df
               .withColumn("prev_mean_x", lag("mean_x").over(w))
               .withColumn("prev_mean_y", lag("mean_y").over(w))
               .withColumn("prev_mean_z", lag("mean_z").over(w))
               .withColumn("distance", 
                           sqrt((col("mean_x") - col("prev_mean_x")) ** 2 +
                                (col("mean_y") - col("prev_mean_y")) ** 2 +
                                (col("mean_z") - col("prev_mean_z")) ** 2))
               .withColumn("prev_distance", lag("distance").over(w))
               .withColumn("move_recommendation",
                           when(col("distance") < col("prev_distance"), "move recommended")
                           .otherwise(None)))

# Starting the streaming queries with personalized query names
standing_recommendation_query = recommendation_df \
    .writeStream \
    .queryName("Lanston_standing_recommendation_results") \
    .format("memory") \
    .outputMode("complete") \
    .start()

move_recommendation_query = distance_df \
    .writeStream \
    .queryName("Lanston_move_recommendation_results") \
    .format("memory") \
    .outputMode("complete") \
    .start()

# Displaying the results for Lanston
print("Standing Recommended Results for Lanston:")
spark.sql("SELECT * FROM Lanston_standing_recommendation_results").show()

print("Move Recommended Results for Lanston:")
spark.sql("SELECT * FROM Lanston_move_recommendation_results").show()

# Stopping the Spark session
spark.stop()
