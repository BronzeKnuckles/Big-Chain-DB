from tkinter import *
from tkinter import ttk

root = Tk()

def printer():
	global e1
	print(e1.get())



e1 = Entry(root)
e1.pack()
b1 = Button(root,text =  "ok",command = printer).pack()



root.mainloop()