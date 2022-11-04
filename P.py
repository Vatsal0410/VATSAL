from math import ceil
from tkinter import *

w = Tk()

w.geometry("500x400")
w.configure(background="lightgreen") #background

favList = ["Cricket","Valleyball","Football"]
allList = ["Netflix","Instagram","Twiter"]

l1 = Label(w,text="Favourite List:",font=("Satisfy",20),fg="white",justify=CENTER,background="lightgreen")
l1.grid(row=0, column=0)

#for i in range(len(favList)):
    #lb1.insert(favList)

l2 = Label(w,text="All List:", font=("Satisfy",20),fg="White",justify=CENTER, background="lightroom")
l2.grid(row=0, column=1)

lb1 = Listbox(w, width=1, height=8, fg="maroon", font=("Times new Roman",16), background="Silver", selectmode="multiple", selectbackground="lightgrey", selectforeground="black", justify=CENTER)
lb1.grid(row=1, column=0, padx=4, pady=55, rowspan=4)

lb2 = Listbox(w, width=1, height=8, fg="maroon", font=("Times new Roman",16), background="silver", selectmode="multiple", selectbackground="lightgrey", selectforeground="black", justify=CENTER)
lb2.grid(row=1, column=3, padx=4, pady=55, rowspan=4)

LtoR_addAll = Button(text=">>",width=10,height=5,justify=CENTER, font=("Satisfy",9))
LtoR_addAll.grid(row=1,column=1,padx=15,pady=2,ipadx=2)



