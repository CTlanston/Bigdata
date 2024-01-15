 Coffee Shop Data Management Project README

 Project Summary
This project involves managing data for a coffee shop using various data loading techniques. The data is sourced from the provided `coffee shop.zip` file and includes different components such as sales receipts, product details, and pastry inventory. The project demonstrates the use of SQL and Python to efficiently load and manage this data.

 Data Sources
- `coffee shop.zip` containing all necessary data files.

 Key Components
1. Sales_receipt: Loaded into the database using SQL's `LOAD DATA LOCAL INFILE` command.
2. Product: A set of 5 entries are manually inserted into the database using the SQL `INSERT INTO` command.
3. Pastry_inventory: Data loaded using Python, with guidance from AWS RDS User Guide on connecting Python with RDS for data operations.

 Project Deliverables
- SQL scripts for loading `Sales_receipt` and `Product` data.
- Python code for loading `Pastry_inventory` data.
- Links to AWS RDS documentation for Python connectivity.

 Usage
- Extract data from `coffee shop.zip`.
- Use the provided SQL scripts for loading specific data sets into a SQL database.
- Execute the Python code to load the pastry inventory, referring to the AWS RDS documentation for any connectivity requirements.

Note: This README is a summary of the project. Detailed instructions and code are provided in the respective SQL and Python files.
