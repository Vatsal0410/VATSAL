from pyexpat.errors import messages
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root =Tk()
root.geometry("500x500")

def click():
    messagebox.showinfo("title","Good Morning")

l1=Label(root, text="Hello World", fg="red").pack()
b1=Button(root, text="Click Here",bg="black",fg="white", command=click).pack()

root.mainloop()