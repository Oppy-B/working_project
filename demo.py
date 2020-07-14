import psycopg2

def createdb():
    conn = psycopg2.connect(dbname= "postgres", user="postgres", password="computer", host="localhost", port="5432")
    cur=conn.cursor()
    cur.execute('''CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT,ADDRESS TEXT);''')
    print('Table created')
    conn.commit()
    conn.close()

def insertdata():
    conn = psycopg2.connect(dbname= "postgres", user="postgres", password="computer", host="localhost", port="5432")
    cur=conn.cursor()
    cur.execute('''INSERT INTO student (NAME,AGE,ADDRESS) VALUES ('ozil','25','london');''')
    print('Table created')
    conn.commit()
    conn.close()

insertdata()


