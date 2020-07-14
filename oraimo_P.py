import psycopg2
from tkinter import *





root = Tk()
root.title('Product Inventory')

def add_button(product, quantity, price, selling_p):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query= '''INSERT INTO oraimo_p(PRODUCT,QUANTITY, COST_P, SELLING_P ) VALUES (%s, %s, %s,%s);'''
    cur= conn.cursor()
    cur.execute(query,(product, quantity, price, selling_p ))
    conn.commit()
    conn.close()
    display_all()

def get_search(product_id):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query = '''SELECT * FROM oraimo_p WHERE product= %s;'''
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
    cur.execute('''SELECT * FROM oraimo_p''')
    row = cur.fetchall()
    listbox1= Listbox(frame, width=30, height=4)
    listbox1.grid(row=12, column=2)    
    for x in row:        
        listbox1.insert(END,x)

    conn.commit()
    conn.close()

def delete(delete_id):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    cur= conn.cursor()
    query = '''DELETE FROM oraimo_p where product=%s;'''
    cur.execute(query, (delete_id,))
    

    conn.commit()
    conn.close()
    display_all()

def edit_row(product, new_price, new_quantity, new_selling):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query= '''UPDATE oraimo_p SET price= %s, quantity= %s, new_selling=%s WHERE product=%s; '''
    cur= conn.cursor()
    cur.execute(query, (new_price, new_quantity, new_selling, product))
    conn.commit()
    conn.close()

    display_all()

def edit_price(product_code, product_price):
    conn = psycopg2.connect(dbname="postgres", user= "postgres", password="computer", host="localhost", port="5432")
    query= '''UPDATE oraimo_p SET SELLING_P= %s WHERE PRODUCT=%s; '''
    cur= conn.cursor()
    cur.execute(query, (product_price, product_code))
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

selling_label= Label(frame,text="Selling price")
selling_label.grid(row=1,column=3)

quantity_label= Label(frame,text="Quantity")
quantity_label.grid(row=2,column=1)

Product_entry = Entry(frame)
Product_entry.grid(row=0,column=2)

price_entry = Entry(frame)
price_entry.grid(row=1,column=2)

selling_entry = Entry(frame)
selling_entry.grid(row=1,column=4)

quantity_entry = Entry(frame)
quantity_entry.grid(row=2,column=2)

button1 = Button(frame, text= "submit", command= lambda: add_button(Product_entry.get(), quantity_entry.get(), price_entry.get(), selling_entry.get()))
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

set_selling= Label(frame, text='New sell price')
set_selling.grid(row=9,column=3)

set_selling_entry= Entry(frame)
set_selling_entry.grid(row=9,column=4)

set_qty= Label(frame, text='Quantity')
set_qty.grid(row=10,column=1)

set_qty_entry= Entry(frame)
set_qty_entry.grid(row=10,column=2)

edit_button= Button(frame, text='Edit', command = lambda: edit_row(edit_entry.get(), set_price_entry.get(), set_qty_entry.get(), set_selling_entry.get() ))
edit_button.grid(row=11,column=2)

edit_code_label = Label(frame, text= 'Enter Product code')
edit_code_label.grid(row=13,column=1)

edit_code_entry= Entry(frame)
edit_code_entry.grid(row=13,column=2)

edit_NewPrice_label = Label(frame, text= 'Enter New price')
edit_NewPrice_label.grid(row=14,column=1)

edit_NewPrice_entry= Entry(frame)
edit_NewPrice_entry.grid(row=14,column=2)

edit_price_button= Button(frame, text='Edit Price', command = lambda: edit_price(edit_code_entry.get(), edit_NewPrice_entry.get() ))
edit_price_button.grid(row=15,column=2)


display_all()

root.mainloop()
