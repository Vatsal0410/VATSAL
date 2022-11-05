from tkinter import * 
import tkinter as tk

top = Tk()
top.geometry("300x200")
var = StringVar()
l = Label(top,text = "")
l.pack()
def printSelection():
	l.config(text="You have selected"+var.get())

r1 = Radiobutton(top,text="Male",variable=var,value="Male",command=printSelection)
r1.pack()
r2 = Radiobutton(top,text="Female",variable=var,value="Female",command=printSelection)
r2.pack()
r3 = Radiobutton(top,text="Other",variable=var,value="Other",command=printSelection)
r3.pack()
top.mainloop()

