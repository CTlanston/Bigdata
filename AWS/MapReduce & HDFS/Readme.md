 MapReduce Theory and Application Project README

 Project Overview
This project is divided into two parts. Part 1 focuses on the theoretical aspect of how the MapReduce processing framework retrieves search results from Twitter data stored in DocumentDB on HDFS, especially for a keyword like "black friday". Part 2 involves practical implementation of MapReduce using AWS EMR and Python to analyze Elon Musk's tweets.

 Part 1: MapReduce Theory (Twitter Data)
 Overview
- Objective: Understanding how MapReduce processes and retrieves search results, including the top 10 tweets and total tweet count, for a specific keyword.
- Data Source: Twitter data stored in DocumentDB on HDFS.

 Key Concepts
- Map Phase: Filter tweets containing "black friday", count occurrences.
- Reduce Phase: Aggregate counts, sort by frequency, and select top 10.
- Handling Large Datasets: Discussion on scalability and efficiency of MapReduce in processing large volumes of Twitter data.

 Part 2: MapReduce on EMR with Python
 Pre-requisites
- AWS EMR CLI setup.
- Installation of `mrjob` library on AWS EMR CLI.
- Dataset: [Elon Musk's Tweets](https://www.kaggle.com/datasets/kulgen/elon-musks-tweets) (data_elonmusk.csv).

 Key Steps
1. Setup AWS EMR and mrjob
   - Launch AWS EMR CLI and install `mrjob`.
2. Data Preparation
   - Create a text file containing tweet text from `data_elonmusk.csv`.
3. Python MapReduce Code
   - Develop a Python script using `mrjob` to identify the most used word in Elon Musk's tweets.
   - Execute the script on the tweet data with Hadoop cluster execution.
4. Analysis and Comparison
   - Note the number of mappers and reducers, and the total time taken for the job.
   - Repeat the task with a smaller dataset (10 tweets) and compare the differences in execution.

 Deliverables
- Python script for MapReduce job on Elon Musk's tweets.
- Documentation including the results, number of mappers/reducers, job completion time, and comparison analysis between the full dataset and a 10-tweet subset.

 Usage
- Follow the theoretical framework in Part 1 to understand the MapReduce process for Twitter data analysis.
- In Part 2, set up AWS EMR and install `mrjob`, then run the provided Python script for tweet analysis.
- Compare and document the differences in MapReduce execution between the two different data sizes.

Note: This README provides an overview of the project's objectives and deliverables. Detailed instructions and code

implementation should be referred to within the respective theoretical framework and Python files provided with the project. The comparison analysis in Part 2 should highlight insights on the performance and scalability aspects of using MapReduce for different data volumes.
