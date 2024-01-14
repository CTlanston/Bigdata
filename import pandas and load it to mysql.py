import pandas as pd
from sqlalchemy import create_engine

# read CSV
df = pd.read_csv("C:\\Program␣Files\\PyCharm\\manage_big_data\\airbnb_nyc_clean.csv")

# create mysql engine
engine =create_engine('mysql+mysqlconnector://root:LnastonChen123456@localhost:3306/bigdata',echo=False)

# load data to mysql
df.to_sql(name='airbnb_nyc', con=engine, if_exists='replace',index=False)