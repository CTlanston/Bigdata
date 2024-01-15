# Hadoop, Hive, and Pig: Yelp and Sakila Data Analysis Project README

## Project Overview
This project involves comprehensive data analysis using Hadoop, Hive, and Pig, focusing on Yelp and Sakila datasets. The objectives include data migration cost analysis, exploring various data loading methods into Hive, and performing comparative performance analysis between Hive and Pig. 

## Data Migration Cost Analysis

### Objective
Calculate and visualize the number of datanodes required for migrating 500TB of data to HDFS and estimate the cost associated with an EMR cluster over 20 quarters.

### Tasks
1. **Datanode Calculation**: Chart the number of datanodes needed for different replication counts. 
2.

**Quarterly Datanode Needs**: Plot changes in datanode requirements every quarter for 20 quarters, assuming a 4% data increase per quarter.
3. **Cost Estimation**: Use the AWS cost calculator to estimate EMR cluster costs based on datanode calculations and projected data growth.

## Data Migration into Hive

### Objective
Explore three different methods of loading happiness data into Hive and analyze their execution times and applicable use cases.

### Tasks
1. **Create Hive Tables**: Set up three tables in Hive (happy1, happy2, happy3).
2. **Data Loading**: Load the happiness data CSV file into RDS MySQL, S3, and then into Hive using various methods.
3. **Execution Time Analysis**: Compare the time taken to load data into Hive across different methods.
4. **Use Case Discussion**: Discuss the scenarios in which each data loading approach would be most suitable.

## Hive vs Pig Performance Analysis

### Objective
Conduct a comparative performance analysis between Hive and Pig using a specific use case and benchmarking exercises.

### Tasks
1. **Literature Review**: Study and discuss use cases where Hive outperforms Pig based on a research paper.
2. **Performance Testing**: Load the 'online-retail-dataset.csv' into both Hive and Pig, executing and benchmarking a specific query in both environments.
3. **Analysis and Reporting**: Present summary statistics of the execution times and discuss any variations and findings in comparison to the paper.

---

**Collaboration and Methodology**
- Engage actively in group discussions to leverage diverse perspectives for a more thorough analysis.
- Experiment with variations in the cluster setup to understand how different configurations impact performance in Hive and Pig.

This project not only highlights technical skills in big data tools like Hadoop, Hive, and Pig but also demonstrates collaborative problem-solving and analytical capabilities.
