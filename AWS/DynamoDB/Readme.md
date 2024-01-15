 AWS DynamoDB with Python Lab Project README

 Project Overview
This project involves completing the AWS lab on using DynamoDB with Python, extending the lab to include JSON data handling. The primary tasks include loading `train.json` data from the Kaggle Recipe Ingredients Dataset into DynamoDB, writing Python scripts to read JSON and put data into DynamoDB, and querying the database to find all ingredients for “Indian” recipes.

 Lab Guide and Data Source
- AWS DynamoDB with Python Lab: [Create and Manage Nonrelational Database with DynamoDB](https://aws.amazon.com/getting-started/hands-on/create-manage-nonrelational-database-dynamodb/)
- Recipe Ingredients Dataset: [train.json on Kaggle](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset)

 Key Steps
1. Complete AWS Lab: Follow the instructions in the AWS lab to set up DynamoDB with Python.
2. Data Preparation: Download `train.json` from the Kaggle Recipe Ingredients Dataset.
3. Load Data into DynamoDB: Develop a Python script (`lab2_load_data.py`) to read the JSON file and load data into DynamoDB.
4. Query DynamoDB: Write another Python script (`lab2_query_dynamodb.py`) to query or scan the database for all ingredients in “Indian” recipes.
5. Documentation: Prepare a PDF document showcasing five results obtained from the query.

 Requirements
- AWS account with access to DynamoDB.
- Python environment with necessary libraries (`boto3`, `json`).
- Access to the Kaggle dataset.

 Project Deliverables
- `lab2_load_data.py`: Python script for loading JSON data into DynamoDB.
- `lab2_query_dynamodb.py`: Python script for querying “Indian” recipe ingredients.
- PDF document: Contains five sample results from the DynamoDB query.

 Usage
- Follow the AWS lab tutorial to set up and configure DynamoDB in your AWS environment.
- Download the `train.json` file and ensure Python with required libraries is set up for script execution.
- Run `lab2_load_data.py` to load data into DynamoDB.
- Execute `lab2_query_dynamodb.py` to retrieve the desired query results.
- Compile the results into a PDF document.

Note: This README provides a summary of the project. Detailed instructions, Python code files, and the methodology for result compilation are provided in the accompanying files.
