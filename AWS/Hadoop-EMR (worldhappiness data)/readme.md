# AWS RDS, S3, EMR, and Oozie Project README

## Project Overview
This project involves several steps to work with AWS services, including RDS, S3, EMR, and Oozie. It includes loading data into an AWS RDS MySQL database, creating an S3 bucket, setting up EMR CLI with Apache Hue, using Sqoop to load data into S3 and HDFS, and finally, using Hue or Oozie XML to manage data workflows.

## Step 1: Load Data in AWS RDS
### Pre-requisites
- World Happiness data: Download `worldhappiness.zip` from the provided source.
- AWS RDS MySQL database setup (named `happiness`).

### Key Steps
1. **Create MySQL Database**: Set up a new schema (`happy`) in MySQL Workbench.
2. **Import Data**: Import CSV files from `worldhappiness.zip` into the `happy` schema.
3. **Modify Primary Key**: Ensure "rank" is set as the primary key in every table.

## Step 2: Create AWS S3 Bucket
### Pre-requisites
- AWS account with S3 service.

### Key Steps
1. **Create S3 Bucket**: Create a bucket named `671happy`.
2. **Create Folder**: Create a folder within the bucket named `671data`.

## Step 3: Setup EMR CLI and Apache Hue
### Pre-requisites
- AWS EMR cluster with m4.large nodes.
- Installation of Sqoop, Oozie, and Hue.

### Key Steps
1. **EMR Cluster Setup**: Follow the provided tutorials to set up the EMR cluster with the necessary services.

## Step 4: Data Load Using Sqoop
### Key Steps
1. **List Tables**: Use Sqoop to list tables in the RDS database.
2. **Load to S3**: Move data from RDS to the AWS S3 bucket using Sqoop.
3. **Load to HDFS**: Transfer data from RDS to HDFS using Sqoop.
4. **Copy Data**: Use `s3-dist-cp` to copy files from S3 to HDFS.

### Deliverables
- Screenshots of CLI showing successful data loads and lists of files in S3 and HDFS.

## Step 5: Use Hue to Browse Data and Run an Oozie Workflow
### Key Steps
1. **Access Hue Interface**: Connect to the Hue Application Interface.
2. **Create Sqoop Scripts**: Develop scripts to import data for two more CSV files.
3. **Oozie Workflow**: Load the Sqoop scripts into an Oozie workflow and add an email notification action.
4. **Run and Monitor Workflow**: Execute

 the workflow in Hue and monitor for completion.

### Deliverables
- Screenshots of the Oozie workflow setup and completion status in Hue.

## Step 5 (Alternate): Create Oozie Workflow XML
### Key Steps
1. **Develop XML Workflow**: Create an Oozie workflow XML file with the provided structure, filling in the specific details such as workflow name, Sqoop action name, namenode IP address, and Sqoop command.
2. **Implement Workflow**: Load the XML file into the Oozie workflow manager and execute it.

### Deliverables
- The Oozie workflow XML file.
- Screenshots or documentation of the workflow execution and results.

## Usage
- Follow the steps sequentially, ensuring all AWS services are properly configured.
- For data loading and workflow management, use the provided guides and tutorials for accurate setup and execution.
- Document each step with screenshots or files as specified in the deliverables.

Note: This README provides an overview of the project's objectives, steps, and deliverables. Detailed instructions and guidance are provided in the accompanying tutorials and resources. Ensure to adhere to AWS best practices and security guidelines throughout the project.
