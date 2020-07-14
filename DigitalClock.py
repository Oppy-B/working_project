from tkinter import *
from datetime import datetime
from dateutil import tz

root = Tk()
canvas = Canvas(root, width = 900, height=700)
canvas.pack()

def local_time():
    now = datetime.now(tz=tz.tzlocal())
    now_str = now.strftime('%H:%M:%S')
    lbl_display_local.config(text=now_str)
    lbl_display_local.after(1000, local_time)

def USA_time():
    now_usa = datetime.now(tz=tz.gettz('America/New_York'))
    now_usa_str = now_usa.strftime('%H:%M:%S')
    lbl_display_USA.config(text=now_usa_str)
    lbl_display_USA.after(1000,USA_time)

def spain_time():
    now_spain = datetime.now(tz=tz.gettz('Europe/Spain'))
    now_spain_str = now_spain.strftime('%H:%M:%S')
    lbl_display_spain.config(text=now_spain_str)
    lbl_display_spain.after(1000,spain_time)


frame1 = Frame()
frame1.place(relx=0.3, rely=0.1, relheight = 0.8, relwidth=0.8)

lbl_local_time = Label(frame1, text = "LOCAL TIME : ", font=('calibri', 20, 'bold'))
lbl_local_time.grid(row=0,column=1)

lbl_display_local = Label(frame1, font=('calibri', 20, 'bold'), background='green', foreground='white')
lbl_display_local.grid(row=0,column=2)



lbl_usa_time = Label(frame1, text = "USA : ", font=('calibri', 20, 'bold'))
lbl_usa_time.grid(row=1,column=1)
lbl_display_USA = Label(frame1, font=('calibri', 20, 'bold'), background='red', foreground='white')
lbl_display_USA.grid(row=1,column=2)



lbl_spain_time = Label(frame1, text = "SPAIN : ", font=('calibri', 20, 'bold'))
lbl_spain_time.grid(row=2,column=1)
lbl_display_spain = Label(frame1, font=('calibri', 20, 'bold'), background='yellow', foreground='white')
lbl_display_spain.grid(row=2,column=2)

local_time()
USA_time()
spain_time()


root.mainloop()