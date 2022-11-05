import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("300x200")
root.title("Radio Button")

def show_selected_size():
    messagebox.showinfo(title='Result', message=selected_size.get())

selected_size=tk.StringVar()
sizes=( ('Small','S'),
        ('Medium','M'),
        ('Large','L'),
        ('Extra Large','XL'),
        ('Extra Extra Large','XXL'))

label = Label(text="What's your t-shirt size ?")
label.pack(fill="x", padx=5, pady=5)

for size in sizes:
    r=Radiobutton(root, text=size[0],value=size[1],variable=selected_size)
    r.pack(fill='x',padx=5,pady=5)

button=Button(root, text="Get Selected Size", command=show_selected_size)
button.pack(fill='x',padx=5,pady=5)

root.mainloop()