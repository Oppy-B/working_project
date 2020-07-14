import psycopg2
import pandas as pd
import pandas.io.sql as psql

conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
print('connected')
cur = conn.cursor()
df = psql.read_sql("Select * from inventory", conn) 

df['Stock_Value'] = df['price'] * df['quantity']
#df.at['Total', 'Stock_Value'] = df['Stock_Value'].sum()
total = df['Stock_Value'].sum()
print(df)

print('Total inventory value is $',total)