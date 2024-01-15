 Spark PageRank Project README

 Project Overview
This project involves building a file of directed web links based on a sample network and using Apache Spark to estimate PageRank values for each webpage. The process includes creating a text file with directed links, loading data into an S3 bucket, and running Spark code to estimate PageRank values under various conditions.

 Data Preparation
 Pre-requisites
- Access to the sample network image for reference.
- AWS account with S3 service.

 Key Steps
1. Create Text File: Develop a text file (`web_links.txt`) containing all directed links based on the sample network. For example:
   ```
   A B
   B C
   C A
   ```

2. Load Data into S3: Upload the `web_links.txt` file to an S3 bucket.

 Spark Code for PageRank Estimation
 Pre-requisites
- Apache Spark setup with access to the data in the S3 bucket.

 Key Steps
1. PageRank Estimation (1 Iteration)
   - Estimate PageRank values for 1 iteration with multiple damping (contribution) factors: 15%, 50%, 85%.
2. PageRank Estimation (Multiple Iterations)
   - Estimate PageRank for 85% contribution factor with multiple iterations: 1, 5, 10, 20.

 Deliverables
- Spark code file(s) for estimating PageRank values.
- Documentation of the results for each condition (different damping factors and iteration counts).

 Usage
- First, create the directed links text file based on

 the sample network and upload it to the S3 bucket.
- Use Spark to load this data and execute the PageRank algorithm.
- Modify the PageRank parameters to estimate values for different damping factors and iteration numbers.
- Document the outcomes of each Spark run, noting the changes in PageRank values with varying conditions.

 Note
- Ensure the Spark environment is properly configured for integration with AWS S3.
- The code should be structured and commented for clarity, especially when adjusting parameters for different runs.
- It's important to analyze and document how PageRank values vary with changes in the damping factor and iteration count, as this will provide insights into the convergence and stability of the PageRank algorithm.

This README provides a guideline for executing the PageRank estimation project using Apache Spark. For detailed implementation, refer to Apache Spark's documentation and the PageRank algorithm's specifications.
