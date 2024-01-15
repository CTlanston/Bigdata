 DocumentDB and NoSQL with Nobel Prize Data Project README

 Project Overview
This project is divided into two parts. Part 1 involves loading Nobel prize data into Amazon DocumentDB and querying the data using Python. Part 2 focuses on creating and manipulating different database schemas in MySQL to hold the Nobel award data.

 Data Source
- Nobel Prize Data: [JSON_Award.json from Kaggle](https://www.kaggle.com/datasets/imdevskp/nobel-prize)

 Part 1: DocumentDB and Python
 Pre-requisites
- Amazon EC2 instance for file upload and access.
- Amazon DocumentDB set up for NoSQL database operations.

 Key Steps
1. Python File: `load_award_data.py`
   - Load all data from `json_award.json` into DocumentDB.
   - Set `awardYear` as the index for efficient querying.
2. Python File: `query_award_data.py`
   - Query to display all awards given out in a selected year.
   - Query to list all award winners in a selected category.

 Deliverables
- `load_award_data.py`: Python script to upload data to DocumentDB.
- `query_award_data.py`: Python script to query awards by year and category.
- Documentation within the Python files for clarity and understanding.

 Part 2: MySQL Database Schemas
 Pre-requisites
- MySQL Database setup.

 Key Steps
1. Schema Creation
   - Nobel_key_value: A key-value schema with one table, two columns (key and value).
   - Nobel_document: A document-based schema with one table representing the entire JSON row.
   - Nobel_column: A column-based schema with multiple tables, each representing a column family.
2. Data Loading
   - Load 3 lines of data into each schema in MySQL.
3. Query Writing
   - Write SQL queries for each schema to display awards given out in a selected year.
4. Size Comparison
   - Estimate and compare the total size of tables in each schema using MySQL's table inspector.

 Deliverables
- SQL scripts and queries for each schema.
- Documentation comparing the estimated total size of tables in each schema.

 Usage
- For Part 1, follow the setup instructions for Amazon EC2 and DocumentDB, and run the provided Python scripts.
- For Part 2, set up the MySQL database schemas as described and execute the SQL scripts.
- Ensure proper documentation and comments are included in all scripts for easy understanding.

Note: This README provides an overview of the project's objectives and deliverables. Detailed instructions

and code implementation should be referred to within the respective Python and SQL files provided with the project.
