# AWS EMR, S3, and pySpark Project README

## Project Overview
This project involves setting up an AWS EMR cluster with various services, creating an S3 bucket to store weblog data, using `distcp` to move data to HDFS, and finally, running Spark SQL code in pySpark to analyze the data.

## Step 1: Create AWS EMR Cluster with Spark
### Pre-requisites
- AWS account with access to EMR service.

### Key Steps
1. **EMR Cluster Setup**: Include Spark, Yarn, Zeppelin, Tez, JupyterHub, Hue, and Hive in the EMR cluster configuration.
2. **Node Selection**: Use `m4.large` nodes and enable Hue.

## Step 2: Create AWS S3 Bucket
### Pre-requisites
- Kaggle account to download the NASA weblog data.

### Key Steps
1. **Download Data**: Get the weblog data from [Kaggle](https://www.kaggle.com/datasets/souhagaa/nasa-access-log-dataset-1995).
2. **Create S3 Bucket**: Make a new bucket on AWS S3 and create a folder named `nasa`.
3. **Upload Data**: Load the downloaded file into the `nasa` folder in your S3 bucket.

## Step 3: Data Transfer using `distcp`
### Key Steps
1. **Data Copy**: Use `distcp` to move data from the S3 `nasa` folder to the HDFS directory `/user/hadoop/nasa/`.

## Step 4: Launch pySpark IDE
### Key Steps
1. **Access EMR CLI**: Use PuTTY SSH to connect to the EMR CLI.
2.

**Connect to Hue**: Follow instructions on the EMR cluster page to connect your browser to the Hue Application Interface.
3. **Launch pySpark IDE**: Start pySpark in either Hue or Jupyter Notebook, as per your preference.

## Step 5: Create Table and Load Data in pySpark
### Key Steps
1. **Load Data**: Use pySpark to load the data from HDFS.
2. **Save as Parquet**: Store the data on HDFS as a parquet file.
3. **Note File Size**: Record the size of the parquet files for reference.

## Step 6: Query Data using Spark SQL
### Analysis Tasks
1. **Top-5 Hosts by File Access**: Identify the top-5 hosts (e.g., `calpoly.edu`) accessing the most files using Spark SQL.
2. **Top-5 Hosts by Data Volume**: Determine the top-5 hosts accessing the most amount of data.
3. **Top-5 Frequently Accessed Files**: Find the top-5 files (e.g., `apollo-10.html`) most frequently accessed.
4. **Top-5 Files by Internet Traffic**: Identify the top-5 files contributing the most to internet traffic.
5. **Repeat with Parquet Data**: Perform the above analyses again using data in parquet format.

### Deliverables
- Instructions and scripts for setting up and configuring the AWS EMR cluster.
- Steps and scripts used for data transfer

 between S3 and HDFS.
- pySpark scripts or Jupyter Notebook files containing the Spark SQL queries for each of the analysis tasks.
- Documentation on the outcomes and insights from the data analysis, including any notable differences in results between CSV and parquet formats.

## Usage
- Follow the steps sequentially, ensuring all AWS services and configurations are correctly set up.
- Execute the pySpark scripts or Jupyter Notebook cells to perform the data analysis tasks.
- Document the process and results, paying particular attention to the efficiency and performance of queries in different data formats.

## Note
- Ensure that you have the necessary permissions and access rights within AWS to create and manage EMR clusters, S3 buckets, and to perform data transfers.
- The analysis should not only focus on obtaining the results but also on understanding the performance implications of different data formats and query structures in Spark SQL.

This README provides a comprehensive guideline for executing a data analysis project using AWS EMR, S3, and pySpark. For detailed implementation, refer to the AWS documentation, Spark SQL guide, and best practices in data analysis and processing.
