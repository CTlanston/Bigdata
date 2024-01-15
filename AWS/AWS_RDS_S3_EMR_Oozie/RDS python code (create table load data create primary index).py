import os
import pandas as pd
from sqlalchemy import create_engine

# Database credentials
host = "database-lab5.c3f4g2yxdyve.us-east-1.rds.amazonaws.com"
port = "3306"
user = "admin"
password = "123456"
database = "happy"

# Directory containing CSV files
directory = "C:\\Users\\ctlan\\OneDrive\\desktop\\manage_bigdata\\assignment\\HW\\hw5\\worldhappiness\\"

# Create a connection to the database
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

# Define a dictionary for the year and its corresponding happiness score column name
happiness_score_columns = {
    '2015.csv': 'Happiness Score',
    '2016.csv': 'Happiness Score',
    '2017.csv': 'Happiness.Score',
    '2018.csv': 'Score',
    '2019.csv': 'Score'
}

# Process each CSV file specified in the dictionary
for filename, happiness_column in happiness_score_columns.items():
    file_path = os.path.join(directory, filename)
    table_name = "happy" + os.path.splitext(filename)[0]  # Use filename without '.csv' as table name

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Standardize column name to 'Happiness Score'
    df.rename(columns={happiness_column: 'Happiness Score'}, inplace=True)

    # Check and standardize country column name
    if 'Country' in df.columns:
        country_column = 'Country'
    elif 'Country or region' in df.columns:
        country_column = 'Country or region'
    else:
        raise ValueError(f'Country column not found in the file {filename}')

    # Sort by 'Happiness Score' and country column, reset index to create 'id' column
    df.sort_values(by=['Happiness Score', country_column], ascending=[False, True], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.index += 1  # Make 'id' start from 1 instead of 0
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)

    # Create or replace the table and load data
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False, chunksize=500)
print(f"Data from {file_path} has been loaded into the {table_name} table.")

print("All specified CSV files have been processed and corresponding tables created.")
