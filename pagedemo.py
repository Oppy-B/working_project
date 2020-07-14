from tkinter import *



'''This class configures and populates the rootlevel window.
root is the rootlevel containing window.'''

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
root = Tk()
root.geometry("600x450+650+150")
root.minsize(148, 1)
root.maxsize(1924, 1055)
root.resizable(1, 1)
root.title("New rootlevel")
root.configure(background="#d9d9d9")

Label1 = Label(root)
Label1.place(relx=0.183, rely=0.156, height=26, width=43)
Label1.configure(background="#d9d9d9")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(text='''name''')

Entry1 = Entry(root)
Entry1.place(relx=0.383, rely=0.156,height=24, relwidth=0.173)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")

    


root.mainloop()