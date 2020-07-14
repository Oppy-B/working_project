import psycopg2

def connect_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="computer", host="localhost", port="5432")
    print("connected to database")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(NAME TEXT, AGE TEXT,ADDRESS TEXT );''')
    conn.commit()
    conn.close()

def insert_value():
    conn = psycopg2.connect(dbname="postgres", user="postgres",password="computer",host="localhost",port="5432")
    name = input("Enter your name")
    age = input("Enter your age")
    address = input("Enter your address")
    cur=conn.cursor()
    query='''INSERT INTO student(NAME,AGE,ADDRESS) VALUES (%s,%s,%s);'''
    cur.execute(query,(name,age,address))
    conn.commit()
    conn.close()

insert_value()