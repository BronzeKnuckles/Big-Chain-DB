from tkinter import *
from tkinter import ttk 
from backend import backend


root = Tk()
root.title("Big Chain DB")


def butt_Create_func():
	create_lab = Label(root,text = "INPUT THE DATA")
	create_lab.pack(side = TOP)
	a = Entry(root)
	a.pack()
	b = Entry(root)
	b.pack()
	
	but = ttk.Button(root,text = "commit",command = lambda:backend.back.docreate(a.get(),b.get()))
	but.pack()
	

	


butt_Create = ttk.Button(root,text = "CREATE", command =butt_Create_func)
butt_Create.pack(side = TOP)



root.mainloop()

root.geometry("500x500")