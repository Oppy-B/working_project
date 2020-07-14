import psycopg2
import pandas as pd
import pandas.io.sql as psql

conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
print('connected')
cur = conn.cursor()
df = psql.read_sql("Select * from oraimo_p", conn) 

df['tcp'] = df['cost_p'] * df['quantity']
df['tsp'] = df['selling_p'] * df['quantity']
#df.at['Total', 'Stock_Value'] = df['Stock_Value'].sum()
total_tcp = df['tcp'].sum()
total_tsp = df['tsp'].sum()
print(df)

print('Total tcp value is #',total_tcp)
print('Total tsp value is #',total_tsp)
profit = total_tsp-total_tcp
print(profit)
