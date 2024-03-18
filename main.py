from tkinter import *

root =Tk()
root.geometry("1200x500")
root.title("Ak's Heading")
root.resizable(False,False)
def Reset():
    entry_Dosa.delete(0,END)
    entry_Idli.delete(0, END)
    entry_Wada.delete(0, END)
    entry_Uttapam.delete(0, END)
    entry_Coffee.delete(0, END)
    entry_juice.delete(0, END)
    entry_Water.delete(0, END)
def Total():
    try:a1=int(Dosa.get())
    except:a1=0

    try:a2=int(Idli.get())
    except:a2=0

    try:a3=int(Wada.get())
    except:a3=0

    try:a4=int(Uttapam.get())
    except:a4=0

    try:a5=int(Coffee.get())
    except:a5=0

    try:a6=int(Juice.get())
    except:a6=0

    try:a7=int(Water.get())
    except:a7=0

    c1 = 60*a1
    c2 = 60*a2
    c3 = 50*a3
    c4 = 80*a4
    c5 = 30*a5
    c6 = 30*a6
    c7 = 20*a7

    lbl_total= Label(f2,font= ("aria",21,'bold'),text = "Total",width=16,fg = "dark blue ",bg= "black")
    lbl_total.place(x=0,y=50)

    entry_total = Entry(f2, font=("aria", 21, 'bold'), textvariable=Total_bill, bd=6, width=6, bg="skyblue")
    entry_total.place(x=20,y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill ="Rs. ",str('%.2f'%totalcost)
    Total_bill.set(string_bill)

Label(text = "Ak Bill Management system", bg ="white",fg = "black", font = ("Times New Roman",21),width = 300, height =2).pack()

f = Frame(root,bg = "sky blue",highlightbackground= "dark blue",highlightthickness=1,width =300,height=370)
f.place(x=30,y=100)

Label(f,text= "MENU", font = ("Gabriola",40,"bold"),bg = "sky blue", fg = "black").place(x=80,y=0)

Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Dosa..........Rs.60/plate",bg = "sky blue", fg = "brown").place(x=30,y=80)
Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Idli..........Rs.60/plate",bg = "sky blue", fg = "brown").place(x=30,y=110)
Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Wada..........Rs.50/plate",bg = "sky blue", fg = "brown").place(x=30,y=140)
Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Uttapam..........Rs.80/plate",bg = "sky blue", fg = "brown").place(x=30,y=170)
Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Coffee..........Rs.30/cup",bg = "sky blue", fg = "brown").place(x=30,y=200)
Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Juice..........Rs.30/glass",bg = "sky blue", fg = "brown").place(x=30,y=230)
Label(f, font = ("Lucida calligraphy",15,"bold"),text = "Water..........Rs.20/bottle",bg = "sky blue", fg = "brown").place(x=30,y=260)


f2 = Frame(root,bg = "dark blue",highlightbackground= "sky blue",highlightthickness=1,width =300,height=370)
f2.place(x=800,y=100)

Bill  =Label(f2,text="Bill",font=("calibri",20),bg = "dark blue")
Bill.place(x=120,y=10)

f1 = Frame(root,bd = 5,width =300,height=370,relief = RAISED)
f1.pack()

Dosa = StringVar
Idli = StringVar
Wada = StringVar
Uttapam = StringVar
Coffee = StringVar
Juice = StringVar
Water = StringVar
Total_bill = StringVar

lbl_Dosa = Label(f1 , font = ("aria",21,"bold"),text = 'Dosa',width = 12 , fg = "White")
lbl_Idli = Label(f1 , font = ("aria",21,"bold"),text = 'Idli',width = 12 , fg = "White")
lbl_Wada = Label(f1 , font = ("aria",21,"bold"),text = 'Wada',width = 12 , fg = "White")
lbl_Uttapam = Label(f1 , font = ("aria",21,"bold"),text = 'Uttapam',width = 12 , fg = "White")
lbl_Coffee = Label(f1 , font = ("aria",21,"bold"),text = 'Coffee',width = 12 , fg = "White")
lbl_juice = Label(f1 , font = ("aria",21,"bold"),text = 'Juice',width = 12 , fg = "White")
lbl_Water = Label(f1 , font = ("aria",21,"bold"),text = 'Water',width = 12 , fg = "White")

lbl_Dosa.grid(row=1,column=0)
lbl_Idli.grid(row=2,column=0)
lbl_Wada.grid(row=3,column=0)
lbl_Uttapam.grid(row=4,column=0)
lbl_Coffee.grid(row=5,column=0)
lbl_juice.grid(row=6,column=0)
lbl_Water.grid(row=7,column=0)

entry_Dosa = Entry(f1,font=("aria",20,'bold'),textvariable=Dosa ,bd=6,width=6,bg="skyblue")
entry_Idli = Entry(f1,font=("aria",20,'bold'),textvariable=Idli ,bd=6,width=6,bg="skyblue")
entry_Wada = Entry(f1,font=("aria",20,'bold'),textvariable=Wada ,bd=6,width=6,bg="skyblue")
entry_Uttapam = Entry(f1,font=("aria",20,'bold'),textvariable=Uttapam ,bd=6,width=6,bg="skyblue")
entry_Coffee = Entry(f1,font=("aria",20,'bold'),textvariable=Coffee ,bd=6,width=6,bg="skyblue")
entry_juice = Entry(f1,font=("aria",20,'bold'),textvariable=Juice ,bd=6,width=6,bg="skyblue")
entry_Water = Entry(f1,font=("aria",20,'bold'),textvariable=Water ,bd=6,width=6,bg="skyblue")

entry_Dosa.grid(row=1,column=1)
entry_Idli.grid(row=2,column=1)
entry_Wada.grid(row=3,column=1)
entry_Uttapam.grid(row=4,column=1)
entry_Coffee.grid(row=5,column=1)
entry_juice.grid(row=6,column=1)
entry_Water.grid(row=7,column=1)


btn_reset = Button(f1,fg = "Black", bg ="Sky Blue", font =("ariel",16,'bold'),width = 10 , text = "Reset",command =Reset)
btn_reset.grid(row=8,column=0)

btn_total = Button(f1,fg = "Black", bg ="Sky Blue", font =("ariel",16,'bold'),width = 10 , text = "Total",command =Total)
btn_total.grid(row=8,column=1)


root.mainloop()