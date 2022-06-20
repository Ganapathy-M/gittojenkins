from tkinter import *
import tkinter.messagebox
import smtplib




g=Tk()
g.title("MENU CARD")
g.geometry("900x700")
g.resizable(0,0)

f2=Frame(g,bd=3,height=370,width=300,relief=RAISED)

#SHAPE
Canvas=Canvas(g,height=520,width=400,relief=RAISED)
Canvas.create_rectangle(0,1,2,3,outline="#ccccff",fill="BLACK",width=3000)
Canvas.place(x=10,y=70)

Chickenbriyani = StringVar()
Muttonbriyani = StringVar()
Nattukozhibriyani = StringVar()
Fishbriyani = StringVar()
Prawnbriyani = StringVar()
Eggbriyani = StringVar()
Mandhibriyani = StringVar()
Chickenrice = StringVar()
Beefrice = StringVar()
Eggrice = StringVar()
Vegrice = StringVar()
prawnrice = StringVar()
Gopirice = StringVar()
Mushroomrice = StringVar()
wish=StringVar()
service_charge=StringVar()
cost=StringVar()
Tax=StringVar()
Total=StringVar()
mail=StringVar()

address=StringVar()
email_body=StringVar()
#FUNCTION

def arul():
       g.destroy()
       
def order():
      tkinter. messagebox.showinfo('ORDER CONFIRMATION','YOURS ORDER IS PLACED AS PER THE YOURS WISH')
 
def generate():
    try:qc=int(Chickenbriyani.get())
    except:qc=0
    try:qm=int(Muttonbriyani.get())
    except:qm=0
    try:qn=int(Nattukozhibriyani.get())
    except:qn=0
    try:qf=int(Fishbriyani.get())
    except:qf=0
    try:qp=int(Prawnbriyani.get())
    except:qp=0
    try:qe=int(Eggbriyani.get())
    except:qe=0
    try:qa=int(Mandhibriyani.get())
    except:qa=0
    try:qcr=int(chickenrice.get())
    except:qcr=0
    try:qbr=int(Beefrice.get())
    except:qbr=0
    try:qer=int(Eggrice.get())
    except:qer=0
    try:qvr=int(Vegrice.get())
    except:qvr=0
    try:qpr=int(Prawnrice.get())
    except:qpr=0
    try:qgr=int(Gopirice.get())
    except:qgr=0
    try:qmr=int(Mushroomrice.get())
    except:qmr=0

    costofChickenbriyani=qc*100
    costofMuttonbriyani=qm*200
    costofNattukozhibriyani=qn*150
    costofFishbriyani=qf*180
    costofPrawnbriyani=qp*180
    costofEggbriyani=qe*80
    costofMandhibriyani=qa*100
    costofChickenrice=qcr*100
    costofBeefrice=qbr*130
    costofEggrice=qer*90
    costofVegrice=qvr*120
    costofPrawnrice=qpr*100
    costofGopirice=qgr*100
    costofMushroomrice=qmr*100

    f2.place(x=550,y=290)
    f2.configure(background="#ccccff")


    ld=Label(f2,text="cost",font="CooperBlack 12",bg="#9999cc")
    ld.grid(row=1,column=0)
    tx=Entry(f2,font=("ariel",12),bd=6,textvariable= cost,width=17,bg="white")
    tx.grid(row=1,column=1)

    ld=Label(f2,text="service charge",font="CooperBlack 12",bg="#9999cc")
    ld.grid(row=2,column=0)
    tx=Entry(f2,font=("ariel",12),bd=6,textvariable=service_charge,width=17,bg="white")
    tx.grid(row=2,column=1)

    ld=Label(f2,text="Tax",font="CooperBlack 12",bg="#9999cc")
    ld.grid(row=3,column=0)
    tx=Entry(f2,font=("ariel",12),bd=6,textvariable=Tax,width=17,bg="white")
    tx.grid(row=3,column=1)

    ld=Label(f2,text="total",font="CooperBlack 12",bg="#9999cc")
    ld.grid(row=4,column=0)
    tx=Entry(f2,font=("ariel",12),bd=6,textvariable=Total,width=17,bg="white")
    tx.grid(row=4,column=1)


    Totalcost=costofChickenbriyani+costofMuttonbriyani+costofNattukozhibriyani+costofFishbriyani+costofPrawnbriyani+costofEggbriyani+costofMandhibriyani+costofChickenrice+costofBeefrice+costofEggrice+costofVegrice+costofPrawnrice+costofGopirice+costofMushroomrice
    costofmeal="Rs",str('%.2f'%Totalcost)
    payTax=(Totalcost*0.18)
    paidTax="Rs",str('%.2f'%payTax)
    ser_charge=(Totalcost*0.01)
    service="Rs",str('%.2f'%ser_charge)
    overall=payTax+Totalcost+ser_charge
    total="Rs",str('%.2f'%overall)


    service_charge.set(service)
    cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)

def out():
       
 Chickenbriyani.set('')
 Muttonbriyani.set('')
 Nattukozhibriyani.set('')
 Fishbriyani.set('')
 Prawnbriyani.set('')
 Eggbriyani.set('')
 Mandhibriyani.set('') 
 Chickenrice.set('')
 Beefrice.set('')
 Eggrice.set('')
 Vegrice.set('')
 prawnrice.set('')
 Gopirice.set('') 
 Mushroomrice.set('')
 wish.set('')
 f2.place_forget()
 address.set('')


def send_message():
        
       sender_mail="gokulnathr998@gmail.com"
       sender_password="rajendiren3019"

       server=smtplib.SMTP('smtp.gmail.com',587)
       
       server.starttls()

       server.login(sender_mail,sender_password)

       print("login ok")

       address_info=address.get()

       email_body_info="yours order is confirmed,enjoy the food ,thanking you "

       server.sendmail(sender_mail,address_info,email_body_info)

       print("mess sended")

    
#label
l1=Label(g,text="vasanth's kitchen",font="CooperBlack 18 bold",bg="RED",relief=RAISED)
l1.place(x=310,y=1)
l1=Label(g,text="FAST FOOD",fg="#FF3300",font="sabon 10  bold")
l1.place(x=370,y=34)
l1=Label(g,text="BRIYANI",fg="#333333",font="garamond 15  ",bg="#9999cc")
l1.place(x=140,y=71)
l1=Label(g,text="1 .Chicken Briyani    Rs=100 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff" )
l1.place(x=20,y=110)
l1=Label(g,text="2 .Mutton Briyani  Rs=200 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=140)
l1=Label(g,text="3 .Nattukozhi Briyani   Rs=150 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=170)
l1=Label(g,text="4 .Fish Briyani     Rs=180 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=200)
l1=Label(g,text="5.Prawns Briyani     Rs=180 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=230)
l1=Label(g,text="6.Egg Briyani     Rs=90 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=260)
l1=Label(g,text="7.Mandhi Briyani     Rs=220 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=290)
l1=Label(g,text="Fried Rice's",fg="#333333",font="garamond 15  ",bg="#9999cc")
l1.place(x=130,y=330)
l1=Label(g,text="1.Chicken rice     Rs=100 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=360)
l1=Label(g,text="2.Beef rice     Rs=130 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=390)
l1=Label(g,text="3.Egg rice     Rs=90 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=420)
l1=Label(g,text="4. Veg-rice     Rs=120 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=450)
l1=Label(g,text="5.Prawn rice     Rs=100 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=480)
l1=Label(g,text="6.Gopi rice     Rs=100 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=510)
l1=Label(g,text="7.Mushroom rice     Rs=100 ",fg="#333333",font="Papyrus 12  ",bg="#ccccff")
l1.place(x=20,y=540)

l1=Label(g,text="customer's wishes",fg="#333333",font="garamond 15  ",bg="#9999cc",relief=RAISED)
l1.place(x=580,y=71)


l1=Label(g,text="customer's e-mailID",fg="#333333",font="garamond 12  ",bg="#9999cc",relief=RAISED)
l1.place(x=580,y=230)

#entry
e1=Entry(g,text=Chickenbriyani)
e1.place(x=300,y=110,width=100) 
e1=Entry(g,text=Muttonbriyani)
e1.place(x=300,y=140,width=100)
e1=Entry(g,text=Nattukozhibriyani)
e1.place(x=300,y=170,width=100,)
e1=Entry(g,text=Fishbriyani)
e1.place(x=300,y=200,width=100)
e1=Entry(g,text=Prawnbriyani)
e1.place(x=300,y=230,width=100)
e1=Entry(g,text=Eggbriyani)
e1.place(x=300,y=260,width=100)
e1=Entry(g,text=Mandhibriyani)
e1.place(x=300,y=290,width=100)
e1=Entry(g,text=Chickenrice)
e1.place(x=300,y=360,width=100)
e1=Entry(g,text=Beefrice)
e1.place(x=300,y=390,width=100)
e1=Entry(g,text=Eggrice)
e1.place(x=300,y=420,width=100)
e1=Entry(g,text=Vegrice)
e1.place(x=300,y=450,width=100)
e1=Entry(g,text=prawnrice)
e1.place(x=300,y=480,width=100)
e1=Entry(g,text=Gopirice)
e1.place(x=300,y=510,width=100)
e1=Entry(g,text=Mushroomrice)
e1.place(x=300,y=540,width=100)
e9=Entry(g,text=wish)
e9.place(x=580,y=110,width=220,height=110)                                    
e11=Entry(g,text=address)
e11.place(x=580,y=260,width=200)                                    

#button
b=Button(g,text="Order Now",command=order)
b.place(x=350,y=630)

b1=Button(g,text="Generate Bill",command=generate)
b1.place(x=450,y=630)

b1=Button(g,text="EXIT",command=arul)
b1.place(x=570,y=630)

b1=Button(g,text="Reset",command=out)
b1.place(x=630,y=630)

b7=Button(g,text="sendmail",command=send_message)
b7.place(x=720,y=630)





g.mainloop()

