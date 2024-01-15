import json
import pymysql

# Read JSON file
with open(r'C:\Users\ctlan\OneDrive\desktop\manage bigdata\assignment\DocumentDB_and_NoSQL\json_award.json', 'r') as f:
    data = json.load(f)

# Connect to MySQL
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='hw4_part2_2',
                             charset='utf8mb4')

#table 2
cursor = connection.cursor()

# Create main table if it doesn't exist
sql_create_table_main = """
CREATE TABLE IF NOT EXISTS Nobel_document (
    index_id INT PRIMARY KEY AUTO_INCREMENT,
    awardYear INT,
    category_en VARCHAR(255),
    category_no VARCHAR(255),
    category_se VARCHAR(255),
    categoryFullName_en VARCHAR(255),
    categoryFullName_no VARCHAR(255),
    categoryFullName_se VARCHAR(255),
    prizeAmount INT,
    prizeAmountAdjusted INT,
    links_rel VARCHAR(255),
    links_href VARCHAR(255),
    links_action VARCHAR(255),
    links_types VARCHAR(255),
    laureate_id VARCHAR(255),
    laureate_name_en VARCHAR(255),
    laureate_portion VARCHAR(255),
    laureate_sortOrder VARCHAR(255),
    laureate_motivation_en VARCHAR(1000),
    laureate_motivation_se VARCHAR(1000),
    laureate_links_rel VARCHAR(255),
    laureate_links_href VARCHAR(255),
    laureate_links_action VARCHAR(255),
    laureate_links_types VARCHAR(255)
);
"""
cursor.execute(sql_create_table_main)
connection.commit()

# Insert JSON data into table
for item in data:
    awardYear = item['awardYear']
    category_en = item['category']['en']
    category_no = item['category']['no']
    category_se = item['category']['se']
    categoryFullName_en = item['categoryFullName']['en']
    categoryFullName_no = item['categoryFullName']['no']
    categoryFullName_se = item['categoryFullName']['se']
    prizeAmount = item['prizeAmount']
    prizeAmountAdjusted = item['prizeAmountAdjusted']
    links_rel = item['links']['rel']
    links_href = item['links']['href']
    links_action = item['links']['action']
    links_types = item['links']['types']
    if 'laureates' in item and item['laureates']:
        laureate = item['laureates'][0]
    else:
        laureate = {}

    laureate_id = laureate.get('id', None)
    laureate_name_en = laureate.get('knownName', {}).get('en', None)
    laureate_portion = laureate.get('portion', None)
    laureate_sortOrder = laureate.get('sortOrder', None)
    laureate_motivation_en = laureate.get('motivation', {}).get('en', None)
    laureate_motivation_se = laureate.get('motivation', {}).get('se', None)
    laureate_links_rel = laureate.get('links', {}).get('rel', None)
    laureate_links_href = laureate.get('links', {}).get('href', None)
    laureate_links_action = laureate.get('links', {}).get('action', None)
    laureate_links_types = laureate.get('links', {}).get('types', None)

    sql = """INSERT INTO Nobel_document (awardYear, category_en, category_no, category_se, categoryFullName_en, categoryFullName_no, categoryFullName_se, prizeAmount, prizeAmountAdjusted, links_rel, links_href, links_action, links_types, laureate_id, laureate_name_en, laureate_portion, laureate_sortOrder, laureate_motivation_en, laureate_motivation_se, laureate_links_rel, laureate_links_href, laureate_links_action, laureate_links_types) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    cursor.execute(sql, (
    awardYear, category_en, category_no, category_se, categoryFullName_en, categoryFullName_no, categoryFullName_se,
    prizeAmount, prizeAmountAdjusted, links_rel, links_href, links_action, links_types, laureate_id, laureate_name_en,
    laureate_portion, laureate_sortOrder, laureate_motivation_en, laureate_motivation_se, laureate_links_rel,
    laureate_links_href, laureate_links_action, laureate_links_types))

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()
