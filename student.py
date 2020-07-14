from tkinter import *
import tkinter as tk
import psycopg2
root = Tk()

def get_variable(name,age,address):
    conn= psycopg2.connect(dbname = "postgres", user= "postgres", password= "computer", host= "localhost", port="5432")
    query= '''INSERT INTO student (NAME,AGE,ADDRESS) VALUES (%s,%s,%s);'''
    cur= conn.cursor()
    cur.execute(query,(name,age,address))
    conn.commit()
    conn.close()
    display_all()

def search_id(id):
    conn=psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    cur=conn.cursor()
    query = '''SELECT * FROM student where id=%s;'''
    cur.execute(query, (id))

    row= cur.fetchone() 

    display_result(row)
    conn.commit()
    conn.close()

def display_result(row):
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=7,column=1)
    listbox.insert(END, row)

def display_all():
    conn=psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    cur=conn.cursor()
    query = '''SELECT * FROM student;'''
    cur.execute(query)
    row=cur.fetchall()

    listbox= Listbox(frame, width=20, height = 7)
    listbox.grid(row=8,column=1)
    for x in row:
        listbox.insert(END,x)

canv = Canvas(root, height = 480, width= 900)
canv.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

label= Label(frame, text="Add data")
label.grid(row=0,column=1)

label= Label(frame, text="NAME")
label.grid(row=1,column=0)

entry_name= Entry(frame)
entry_name.grid(row=1,column=1)

label= Label(frame, text="AGE")
label.grid(row=2,column=0)

entry_age= Entry(frame)
entry_age.grid(row=2,column=1)

label= Label(frame, text="ADDRESS")
label.grid(row=3,column=0)

entry_address= Entry(frame)
entry_address.grid(row=3,column=1)

button = Button(frame, text= "ADD", command= lambda: get_variable(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

label = Label(frame, text= "SEARCH")
label.grid(row=5,column=1)

label = Label(frame, text="SEARCH ID")
label.grid(row=6, column=0)

id_entry= Entry(frame)
id_entry.grid(row=6,column=1)

button1= Button(frame, text="search",command= lambda: search_id(id_entry.get()))
button1.grid(row=6,column=2)

display_all()

root.mainloop()

