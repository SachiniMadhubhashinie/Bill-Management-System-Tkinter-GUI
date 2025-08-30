from tkinter import*

root=Tk()
root.geometry("900x400")
root.title("Bill Management")
root.resizable(False, False)
def Reset():
    Entry_Dosa.delete(0, END)
    Entry_Cookies.delete(0, END)
    Entry_Tea.delete(0, END)
    Entry_Coffee.delete(0, END)
    Entry_Juice.delete(0, END)
    Entry_Pancakes.delete(0, END)
    Entry_Eggs.delete(0, END)


def Total():
    try: a1 = int(Dosa.get())
    except: a1 = 0
    try: a2 = int(Cookies.get())
    except: a2 = 0
    try: a3 = int(Tea.get())
    except: a3 = 0
    try: a4 = int(Coffee.get())
    except: a4 = 0
    try: a5 = int(Juice.get())
    except: a5 = 0
    try: a6 = int(Pancakes.get())
    except: a6 = 0
    try: a7 = int(Eggs.get())
    except: a7 = 0

    # define cost of each item per quantity
    c1 = a1 * 60
    c2 = a2 * 30
    c3 = a3 * 7
    c4 = a4 * 100
    c5 = a5 * 20
    c6 = a6 * 15
    c7 = a7 * 7

    # Remove previous total if any
    for widget in f2.winfo_children():
        if isinstance(widget, Entry) or (isinstance(widget, Label) and widget.cget("text").startswith("Rs.")):
            widget.destroy()

    lbl_total = Label(f2, font=("arial", 16, "bold"), text="Total", width=16, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=40)

    entry_total = Entry(f2, font=("arial", 16, "bold"), textvariable=Your_Total_Bill, width=16, bd=4, bg="lightgreen")
    entry_total.place(x=10, y=80)

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    string_bill = "Rs. %.2f" % totalcost
    Your_Total_Bill.set(string_bill)


# Title Bar
Label(root, text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 28, "bold"), width=900, height=2, anchor="center").place(x=0, y=0)



# MENU CARD (Left Panel)
f=Frame(root,bg= "lightgreen", highlightbackground="black", highlightthickness=1,width=250,height=300)
f.place(x=10,y=70)

Label(f,text="Menu", font= ("Gabriola", 24,"bold"), fg="black", bg="lightgreen").place(x=70,y=5)

Label(f, font= ("arial", 12, "bold"), text ="Dosa........Rs.60/plate",fg="black",bg="lightgreen", anchor="w").place(x=10,y=50)
Label(f, font= ("arial", 12, "bold"), text ="Cookies.....Rs.30/plate",fg="black",bg="lightgreen", anchor="w").place(x=10,y=75)
Label(f, font= ("arial", 12, "bold"), text ="Tea........Rs.7/cup",fg="black",bg="lightgreen", anchor="w").place(x=10,y=100)
Label(f, font= ("arial", 12, "bold"), text ="Coffee.....Rs.100/cup",fg="black",bg="lightgreen", anchor="w").place(x=10,y=125)
Label(f, font= ("arial", 12, "bold"), text ="Juice......Rs.20/glass",fg="black",bg="lightgreen", anchor="w").place(x=10,y=150)
Label(f, font= ("arial", 12, "bold"), text ="Pancakes...Rs.15/pack",fg="black",bg="lightgreen", anchor="w").place(x=10,y=175)
Label(f, font= ("arial", 12, "bold"), text ="Eggs.......Rs.7/egg",fg="black",bg="lightgreen", anchor="w").place(x=10,y=200)



# Bill (Right Panel)
f2=Frame(root,bg="lightyellow",highlightbackground="black", highlightthickness=1,width=250,height=300)
f2.place(x=630,y=70)
Bill=Label(f2,text="Bill", font=("calibri", 20, "bold"), bg="lightyellow")
Bill.place(x=100,y=10)




# ENTRY WORK (Middle Panel)
f1=Frame(root,bd=2,height=300,width=250,relief=RAISED, bg="white")
f1.place(x=270,y=70)

# Variables for new menu
Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Pancakes=StringVar()
Eggs=StringVar()
Your_Total_Bill=StringVar()

# Labels
lbl_Dosa=Label(f1,  font=("arial", 14, "bold"),text="Dosa",width=10, fg="blue4", bg="white")
lbl_Cookies=Label(f1,  font=("arial", 14, "bold"),text="Cookies",width=10, fg="blue4", bg="white")
lbl_Tea=Label(f1,  font=("arial", 14, "bold"),text="Tea",width=10, fg="blue4", bg="white")
lbl_Coffee=Label(f1,  font=("arial", 14, "bold"),text="Coffee",width=10, fg="blue4", bg="white")
lbl_Juice=Label(f1,  font=("arial", 14, "bold"),text="Juice",width=10, fg="blue4", bg="white")
lbl_Pancakes=Label(f1,  font=("arial", 14, "bold"),text="Pancakes",width=10, fg="blue4", bg="white")
lbl_Eggs=Label(f1,  font=("arial", 14, "bold"),text="Eggs",width=10, fg="blue4", bg="white")

lbl_Dosa.grid(row=0, column=0, pady=2)
lbl_Cookies.grid(row=1, column=0, pady=2)
lbl_Tea.grid(row=2, column=0, pady=2)
lbl_Coffee.grid(row=3, column=0, pady=2)
lbl_Juice.grid(row=4, column=0, pady=2)
lbl_Pancakes.grid(row=5, column=0, pady=2)
lbl_Eggs.grid(row=6, column=0, pady=2)

# Entry
Entry_Dosa=Entry(f1, font=("arial", 14, "bold"), textvariable=Dosa, width=8, bd=3,bg="pink")
Entry_Cookies=Entry(f1, font=("arial", 14, "bold"), textvariable=Cookies, width=8, bd=3,bg="pink")
Entry_Tea=Entry(f1, font=("arial", 14, "bold"), textvariable=Tea, width=8, bd=3,bg="pink")
Entry_Coffee=Entry(f1, font=("arial", 14, "bold"), textvariable=Coffee, width=8, bd=3,bg="pink")
Entry_Juice=Entry(f1, font=("arial", 14, "bold"), textvariable=Juice, width=8, bd=3,bg="pink")
Entry_Pancakes=Entry(f1, font=("arial", 14, "bold"), textvariable=Pancakes, width=8, bd=3,bg="pink")
Entry_Eggs=Entry(f1, font=("arial", 14, "bold"), textvariable=Eggs, width=8, bd=3,bg="pink")

Entry_Dosa.grid(row=0, column=1, pady=2)
Entry_Cookies.grid(row=1, column=1, pady=2)
Entry_Tea.grid(row=2, column=1, pady=2)
Entry_Coffee.grid(row=3, column=1, pady=2)
Entry_Juice.grid(row=4, column=1, pady=2)
Entry_Pancakes.grid(row=5, column=1, pady=2)
Entry_Eggs.grid(row=6, column=1, pady=2)



# Buttons
btn_reset=Button(f1,bd=2,fg="black",font=("arial", 14, "bold"), text="Reset", width=10, bg="lightblue",command=Reset)
btn_reset.grid(row=7, column=0, pady=10)

btn_total=Button(f1,bd=2,fg="black",font=("arial", 14, "bold"), text="Total", width=10, bg="lightblue",command=Total)
btn_total.grid(row=7, column=1, pady=10)


root.mainloop()