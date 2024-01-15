*Hadoop, Hive, and Pig - Analysis of Yelp and Sakila Datasets

**Due Date:** November 17, 2023, 8:30 PM  
**Points:** 30  
**Submission:** One file upload, File Types: PDF  
**Late Penalty:** 20% deduction for every 12-hour delay

---

**Question 1: Data Migration Costs**

- **Objective:** Calculate and plot the number of datanodes needed for migrating 500TB of data to HDFS with different data replication counts. Additionally, project the cost associated with an EMR cluster over the next 20 quarters, accounting for a 4% quarterly data increase.
- **Skills Demonstrated:** Data migration planning, HDFS storage calculations, cost estimation using AWS cost calculator.
- **Tasks:**
    1. **Datanode Calculation**:

      - Create a chart showing the number of datanodes required based on different data replication counts.
      - For a replication count of 3, plot the change in datanode needs every quarter for the next 20 quarters, considering a 4% data increase each quarter.
    2. **Cost Estimation**:
      - Utilize the AWS cost calculator to estimate the cost of the EMR cluster, based on the number of datanodes calculated and an 80% utilization rate. Assume a linear increase in price over time.

**Question 2: Data Migration into Hive**

- **Objective:** Explore different methods of loading data into Hive and discuss their execution times and use cases.
- **Skills Demonstrated:** Data loading in Hive, use of RDS, S3, Sqoop, and HiveQL.
- **Tasks:**
    1. **Data Loading**:
      - Create three Hive tables (happy1, happy2, happy3).
      - Load a happiness data CSV file into RDS MySQL (data1), S3 (data2), and then into Hive through various methods.
    2. **Execution Time Analysis**:
      - Compare the execution time for each method of data loading.
    3. **Use Case Discussion**:
      - Discuss the appropriate use cases for each data loading approach.

**Question 3: Hive vs Pig**

- **Objective:** Compare Hive and Pig in terms of performance based on a specific use case and personal experimentation.
- **Skills Demonstrated:** Comparative analysis of Hive and Pig, execution time benchmarking.
- **Tasks:**
    1. **Case Study Review**:
      - Review the findings from the provided research paper and discuss use cases where Hive outperforms Pig.
    2. **Performance Testing**:
      - Load online-retail-dataset.csv into both Hive and Pig.
      - Execute a query to find orders with UnitPrice > 5 and Quantity < 10 in both environments.
      - Repeat the query 10 times and record execution times.
    3. **Analysis**:
      - Report summary statistics (mean, min, max, stddev) of the execution times.
      - Discuss any observed variations and compare findings with the research paper.

---

**Collaboration Tips:**
- Engage in group discussions to understand each team member's perspective and objectives. Collective efforts often lead to more comprehensive solutions.
- Experiment with different EMR clusters within the group to see how variations affect execution times, especially in the Hive vs Pig comparison. This collaborative approach can provide a broader understanding of the tools' performance under different conditions.
