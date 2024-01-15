import json
import pymysql

# Read JSON file
with open(r'C:\Users\ctlan\OneDrive\desktop\manage bigdata\assignment\DocumentDB and NoSQL\json_award.json', 'r') as f:
    data = json.load(f)

# Connect to MySQL
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='hw4_part2_1',
                             charset='utf8mb4')

cursor = connection.cursor()

# Create table if it doesn't exist
sql_create_table = """
CREATE TABLE IF NOT EXISTS nobel_key_valu (
    index_id INT PRIMARY KEY AUTO_INCREMENT,
    data JSON NOT NULL
);
"""
cursor.execute(sql_create_table)
connection.commit()

# Insert JSON data into table
for i, item in enumerate(data):
    if i >= 3:  # Stop after inserting 3 rows
        break
    sql = "INSERT INTO nobel_key_valu (data) VALUES (%s);"
    cursor.execute(sql, (json.dumps(item),))

# Commit changes and close connection
connection.commit()
connection.commit()
cursor.close()
connection.close()
