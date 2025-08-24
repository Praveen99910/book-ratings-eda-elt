import pandas as pd 
import mysql.connector as sql
data = pd.read_csv('final_proj.csv')
data
connection = sql.connect(host= 'localhost',
                         user='root',
                         passwd= 'Pr@veen99910',
                         database='sql_new')
connection
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:Pr%40veen99910@localhost:3306/elt_project")
engine
data.to_sql('final_proj', engine, index= False ,if_exists='append',chunksize=5000)
pd.read_sql('''select * from final_proj''',engine)
%history -f ELT.py
