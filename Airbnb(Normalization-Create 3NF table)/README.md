# Airbnb Data Analysis Project README

## Project Overview
This project focuses on designing a database using Airbnb's open data available on Kaggle. The primary objectives include importing the data into MySQL, normalizing the data to the Third Normal Form (3NF) using the IDTKNI process, and developing a conceptual design of the database. The final output includes the first five rows of each table, all table relationships, and an Entity-Relationship (ER) model of the normalized data.

## Data Source
- Primary Source: [Kaggle Airbnb Open Data](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata)
- Alternative Source: [Kaggle Airbnb NYC Cleaned Data](https://www.kaggle.com/datasets/sandeepmajumdar/airbnbnyccleaned)

## Tools Used
- MySQL for database creation and management.
- ER modeling tools for reverse engineering to get the ER Model.

## Methodology: IDTKNI Process
1. **Identify Data Elements:** Examine the datasets to identify all the distinct data elements.
2. **Divide Data Elements:** Split the data elements into logical groupings.
3. **Identify Tables:** Create tables based on the logical groupings of data elements.
4. **Identify Keys:** Determine primary and foreign keys for each table.
5. **Normalize:** Normalize the data up to the Third Normal Form (3NF).
6. **Develop Index:** Create indices for efficient data retrieval.

## Steps
1. **Data Import:** Import the dataset into MySQL.
2. **Normalization Process:** Apply the IDTKNI process step-by-step, updating the database tables accordingly.
3. **Create and Populate Tables:** Develop the MySQL tables as per the normalized structure and populate them with data.
4. **Conceptual Design Development:** Develop a conceptual design of the database, outlining all tables and their relationships.
5. **Relationships and Keys:** Establish relationships between tables, adding new keys where necessary.
6. **ER Model:** Use a reverse engineering process to create the ER model of the normalized data.

## Submission Contents
1. **Normalized Tables:** The first 5 rows of each table in the database.
2. **ER Diagram:** The ER model illustrating the structure and relationships of the database.

## Running the Project
- Ensure MySQL is installed and properly configured on your system.
- Import the dataset from Kaggle into your MySQL environment.
- Follow the steps outlined in the methodology to create and populate the database.
- Utilize an ER modeling tool to reverse engineer and generate the ER diagram.

## Notes
- The database design is based on the datasets provided and may need adjustments for other similar datasets.
- Ensure to regularly backup the database during the normalization process to avoid data loss.
