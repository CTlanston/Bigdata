 Sakila Database Query Project README

 Project Overview
This project entails querying the Sakila database, a sample database provided by MySQL, using Python. The primary objective is to connect to the AWS Academy RDS MySQL instance, load the Sakila database, and write a Python script to query the top five film genres based on gross revenue in descending order.

 Data Source
- Sakila Database: Downloadable from [MySQL Documentation](https://dev.mysql.com/doc/index-other.html).

 Key Steps
1. Database Setup: Connect to the AWS RDS endpoint using MySQL Workbench and load the Sakila database.
2. Query Development: Write a SQL query to find the top five film genres by gross revenue, in descending order. (Reference: Slide 38 in the "SQL II" lecture).
3. Python Integration: Develop a Python script to execute the SQL query and retrieve results.

 Requirements
- MySQL Workbench for database connection and setup.
- Python environment with necessary libraries (e.g., `mysql-connector-python`) to run the query and handle database connections.

 Project Deliverables
- Python script that connects to the Sakila database on AWS RDS and executes the query.
- The output of the query, showing the top five film genres by gross revenue.

 Usage
- Ensure MySQL Workbench is installed and properly set up to connect to AWS RDS.
- Download and load the Sakila database into the AWS RDS MySQL instance.
- Run the provided Python script to execute the query. Ensure Python and required libraries are installed.

Note: This README provides a summary of the project. Detailed instructions and the Python code are included in the accompanying files.
