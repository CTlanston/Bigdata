import json
import pymysql

# Establish MySQL connection
conn = pymysql.connect(host='localhost', user='root', password='123456', db='hw4_part2_3')
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS nobel_main (
    index_id INT PRIMARY KEY AUTO_INCREMENT,
    awardYear INT,
    prizeAmount INT,
    prizeAmountAdjusted INT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nobel_category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_en VARCHAR(50),
    category_no VARCHAR(50),
    category_se VARCHAR(50),
    categoryFullName_en TEXT,
    categoryFullName_no TEXT,
    categoryFullName_se TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nobel_links (
    link_id INT PRIMARY KEY AUTO_INCREMENT,
    rel VARCHAR(50),
    href TEXT,
    action VARCHAR(50),
    types VARCHAR(50)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nobel_laureates (
    laureate_id INT PRIMARY KEY AUTO_INCREMENT,
    knownName_en VARCHAR(100),
    portion VARCHAR(10),
    sortOrder VARCHAR(10),
    motivation_en TEXT,
    motivation_se TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nobel_laureate_links (
    laureate_link_id INT PRIMARY KEY AUTO_INCREMENT,
    rel VARCHAR(50),
    href TEXT,
    action VARCHAR(50),
    types VARCHAR(50)
);
""")

# Read JSON file
with open(r'C:\Users\ctlan\OneDrive\desktop\manage bigdata\assignment\DocumentDB_and_NoSQL\json_award.json', 'r') as f:
    data = json.load(f)

# Insert data
for item in data:
    cursor.execute("INSERT INTO nobel_main (awardYear, prizeAmount, prizeAmountAdjusted) VALUES (%s, %s, %s);",
                   (item['awardYear'], item['prizeAmount'], item['prizeAmountAdjusted']))
    main_id = cursor.lastrowid

    category = item['category']
    cursor.execute(
        "INSERT INTO nobel_category (category_en, category_no, category_se, categoryFullName_en, categoryFullName_no, categoryFullName_se) VALUES (%s, %s, %s, %s, %s, %s);",
        (category['en'], category['no'], category['se'], item['categoryFullName']['en'], item['categoryFullName']['no'],
         item['categoryFullName']['se']))

    links = item['links']
    cursor.execute("INSERT INTO nobel_links (rel, href, action, types) VALUES (%s, %s, %s, %s);",
                   (links['rel'], links['href'], links['action'], links['types']))

    if 'laureates' in item:
        for laureate in item['laureates']:
            knownName_en = laureate['knownName']['en'] if 'knownName' in laureate and 'en' in laureate[
                'knownName'] else None
            portion = laureate['portion'] if 'portion' in laureate else None
            sortOrder = laureate['sortOrder'] if 'sortOrder' in laureate else None
            motivation_en = laureate['motivation']['en'] if 'motivation' in laureate and 'en' in laureate[
                'motivation'] else None
            motivation_se = laureate['motivation']['se'] if 'motivation' in laureate and 'se' in laureate[
                'motivation'] else None

            cursor.execute(
                "INSERT INTO nobel_laureates (knownName_en, portion, sortOrder, motivation_en, motivation_se) VALUES (%s, %s, %s, %s, %s);",
                (knownName_en, portion, sortOrder, motivation_en, motivation_se))

            laureate_links = laureate['links']
            cursor.execute("INSERT INTO nobel_laureate_links (rel, href, action, types) VALUES (%s, %s, %s, %s);",
                           (laureate_links['rel'], laureate_links['href'], laureate_links['action'],
                            laureate_links['types']))

    conn.commit()

# Close connection
cursor.close()
conn.close()
