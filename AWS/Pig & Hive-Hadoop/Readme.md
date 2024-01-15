# Hadoop Ecosystem Technologies Project README

## Project Overview
This project is divided into three parts. The first part involves discussing the role of various Hadoop ecosystem technologies. The second and third parts involve practical implementation of Pig and Hive scripts for processing NYSE stock data and tripdata, respectively. An additional task includes writing scripts to parse and analyze web log data.

## Part 1: Discussing Hadoop Ecosystem Technologies
### Technologies to Discuss
- **Yarn**: Discuss its role in resource management and job scheduling.
- **Zookeeper**: Explain its importance in configuration management and cluster coordination.
- **Oozie**: Cover its use as a workflow scheduler for Hadoop jobs.
- **Sqoop**: Describe how it is used for efficient data transfer between Hadoop and relational databases.
- **Hue**: Discuss its role as a web interface for interacting with Hadoop.

### Deliverable
- A one-page document discussing the roles of the above Hadoop ecosystem technologies.

## Part 2: Pig Script for NYSE Stock Data
### Pre-requisites
- NYSE stock data: Upload daily and dividend data to S3 bucket.
- Apache Pig setup for running Pig scripts.

### Key Steps
1. **Load Data into Pig**: Use Pig shell (grunt) to load daily and dividend files.
2. **Data Processing**: Join the data on stock and date, calculate dividend/close_price, and identify min/max values.
3. **Script Creation**: Develop a Pig script (`nyse.pig`) to execute the above steps.

### Deliverable
- The `nyse.pig` script file.

## Part 3: Hive Queries for Trip Data
### Pre-requisites
- Tripdata: Upload `tripdata.csv` to a folder in S3 bucket.
- Apache Hive setup for executing HiveQL queries.

### Key Steps
1. **Create External Table**: Define a Hive external table `nyTaxi` with appropriate columns, terminators, and storage location.
2. **Query Execution**: Execute HiveQL queries to get distinct `rate_code_id` and show rows where `rate_code_id = 1`.
3. **Script Creation**: Write the Hive queries in a text file (`nytaxi.hql`).

### Deliverable
- The `nytaxi.hql` script file.

## Part 4: Shell, Pig, and Hive Scripts for Weblog Data
### Pre-requisites
- Weblog data: Upload to S3 bucket.

### Key Steps
1. **Pig Script (`logs.pig`)**: Write a Pig script to parse the weblog data into the desired format and store in HDFS.
2. **HiveQL Script (`logs.hql`)**: Develop a HiveQL script to query the parsed data for the count of 404 errors per IP address.
3. **Shell Script (`logs.sh`)**: Create a shell script to

 execute both the Pig and Hive scripts sequentially.

### Deliverables
- `logs.pig`: Pig script for parsing and storing weblog data.
- `logs.hql`: HiveQL script for querying the parsed data.
- `logs.sh`: Shell script to run the Pig and Hive scripts.

## Usage
- For Part 1, prepare a concise document detailing the role of each Hadoop technology.
- In Part 2, use Pig to process the NYSE stock data as per the instructions and save the script as `nyse.pig`.
- For Part 3, execute the defined HiveQL queries on the trip data and save the script as `nytaxi.hql`.
- In Part 4, develop the required scripts to parse and analyze

 weblog data, ensuring each script (`logs.pig`, `logs.hql`, `logs.sh`) performs its designated task correctly.

## Note
- Ensure all scripts are well-documented for clarity and ease of understanding.
- Test each script individually to confirm its functionality before integrating them into the workflow.
- Adhere to best practices in scripting and data processing to ensure efficient and error-free execution.

This README provides a structured approach to tackling the project's objectives across different Hadoop ecosystem technologies and tools. For detailed guidance on script development and execution, refer to the respective documentation of Pig, Hive, and other relevant technologies.
