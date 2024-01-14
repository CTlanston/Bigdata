# CONNECTED WITH AWS RDS
import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
from sqlalchemy import create_engine

config = {
    'user': 'TCHE368',
    'password':'AUGmRwkd$5',
    'host': "msba2024-serverless-mysql-production.cluster-cqxikovybdnm.us-east-2.rds.amazonaws.com",
    'port': 3306,
    'database': "STUDENT_TCHE368",
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'SSLCERTIFICATE'
}

try:
    conn = mysql.connector.connect(**config)
    cur = conn.cursor()
    cur.execute('SELECT NOW()')
    print(cur.fetchone())
except Exception as e:
    print(f"Database connection failed due to {e}")



# read CSV
conn_str = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

# create mysql engine
engine = create_engine(conn_str)

# load data to mysql
df = pd.read_csv("C:\Program Files\MySQL\MySQL Workbench 8.0\manage_bigdata\HW3\pastry inventory.csv")
df.to_sql(name='pastry_inventory', con=engine, if_exists='replace',index=False)
