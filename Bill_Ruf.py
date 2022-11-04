from tkinter import *
import tkinter as tk



root = Tk()
root.title("Bill")
root.geometry("500x300")

bill=0

def Calculate():
    print("Hello")

W=Label(root, text="Food Menu", font="50")
Checkbutton1 = tk.IntVar()
Checkbutton2 = tk.IntVar()
Checkbutton3 = tk.IntVar()
Checkbutton4 = tk.IntVar()

Button1 = Checkbutton(root, text="Pizza 500", variable=Checkbutton1, onvalue=1, offvalue=0, height=2, width=10)
Button2 = Checkbutton(root, text="Dosa 200", variable=Checkbutton2, onvalue=1, offvalue=0, height=2, width=10)
Button3 = Checkbutton(root, text="Maggie 100", variable=Checkbutton3, onvalue=1, offvalue=0, height=2, width=10)
Button4 = Checkbutton(root, text="Cold Drink 150", variable=Checkbutton4, onvalue=1, offvalue=0, height=2, width=10)

calculate = Button(root, text="Total", height=2, width=10, command=Calculate)

l = Label(root, text="Your total bill is : %s"%(bill))

W.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Calculate.pack()
l.pack()

root.mainloop()