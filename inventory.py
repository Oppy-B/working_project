import psycopg2
from tkinter import *





root = Tk()
root.title('Product Inventory')

def add_button(product, price, quantity):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query= '''INSERT INTO inventory(PRODUCT, PRICE, QUANTITY) VALUES (%s, %s, %s);'''
    cur= conn.cursor()
    cur.execute(query,(product, price, quantity))
    conn.commit()
    conn.close()
    display_all()

def get_search(product_id):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query = '''SELECT * FROM inventory WHERE product= %s;'''
    cur= conn.cursor()
    cur.execute(query,(product_id,))
    row = cur.fetchone()
    listbox1= Listbox(frame, width=20, height=1)
    listbox1.grid(row=6, column=2)
    listbox1.insert(END,row)

    conn.commit()
    conn.close()

def display_all():
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    cur= conn.cursor()
    cur.execute('''SELECT * FROM inventory''')
    row = cur.fetchall()
    listbox1= Listbox(frame, width=20, height=4)
    listbox1.grid(row=12, column=2)    
    for x in row:        
        listbox1.insert(END,x)

    conn.commit()
    conn.close()

def delete(delete_id):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    cur= conn.cursor()
    query = '''DELETE FROM inventory where product=%s;'''
    cur.execute(query, (delete_id,))
    

    conn.commit()
    conn.close()
    display_all()

def edit_row(product, new_price, new_quantity):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query= '''UPDATE inventory SET price= %s, quantity= %s WHERE product=%s; '''
    cur= conn.cursor()
    cur.execute(query, (new_price, new_quantity, product))
    conn.commit()
    conn.close()

    display_all()





canvas=Canvas(root, height = 700, width = 900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely= 0.1, relheight=0.8, relwidth=0.8)

product_label= Label(frame, text= "Product Name")
product_label.grid(row=0,column=1)

price_label= Label(frame,text="Product price")
price_label.grid(row=1,column=1)

quantity_label= Label(frame,text="Quantity")
quantity_label.grid(row=2,column=1)

Product_entry = Entry(frame)
Product_entry.grid(row=0,column=2)

price_entry = Entry(frame)
price_entry.grid(row=1,column=2)

quantity_entry = Entry(frame)
quantity_entry.grid(row=2,column=2)

button1 = Button(frame, text= "submit", command= lambda: add_button(Product_entry.get(), price_entry.get(), quantity_entry.get()))
button1.grid(row=3,column=2)

delete_label= Label(frame, text= 'Delete Product')
delete_label.grid(row=4,column=1)

delete_entry= Entry(frame)
delete_entry.grid(row=4,column=2)
delete_button= Button(frame, text='delete', command = lambda: delete(delete_entry.get()) )
delete_button.grid(row=4,column=3)




search_label= Label(frame, text= 'Search Product')
search_label.grid(row=5,column=1)
search_entry= Entry(frame)
search_entry.grid(row=5,column=2)
search_button= Button(frame, text='Search', command = lambda: get_search(search_entry.get()))
search_button.grid(row=5,column=3)

edit_label = Label(frame, text= 'Edit')
edit_label.grid(row=7,column=2)

edit_name= Label(frame, text='Enter Product name')
edit_name.grid(row=8,column=1)

edit_entry= Entry(frame)
edit_entry.grid(row=8,column=2)

set_price= Label(frame, text='New price')
set_price.grid(row=9,column=1)

set_price_entry= Entry(frame)
set_price_entry.grid(row=9,column=2)

set_qty= Label(frame, text='Quantity')
set_qty.grid(row=10,column=1)

set_qty_entry= Entry(frame)
set_qty_entry.grid(row=10,column=2)

edit_button= Button(frame, text='Edit', command = lambda: edit_row(edit_entry.get(), set_price_entry.get(), set_qty_entry.get() ))
edit_button.grid(row=11,column=2)


display_all()

root.mainloop()
