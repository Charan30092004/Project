from tkinter import *
from AdditionalFunctions import *
from tkinter import messagebox
import mysql.connector


def sub(t):

    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
    mycursor=address.cursor()

    name=e.get()
    vno=e1.get()
    model=e2.get()
    no_of_owners=e3.get()
    pre_owner=e4.get()
    current_owner=e5.get()
    currentfuel=e6.get()
    currentfuel=currentfuel.replace(" ",'')
    currenttype=e7.get()
    currenttype=currenttype.replace(" ",'')
    insurance_renewal=e8.get()
    owner_no=e9.get()
    owner_addrs=e10.get()
    clr()


    checkphone=checkPhoneNumber(owner_no)
    if(not checkphone):
        messagebox.showerror("Enter a Valid Number")

    mycursor.execute("INSERT INTO `maintable` ( `Name`, `VehicleNumber`, `Vehicle Model`, `Number of Owner`, `Previous Owner`, `Fuel`, `Type`, `Insurance`, `Owner Mobile Number`, `Owner Address`) VALUES ( %s, %s, %s, %s,%s, %s, %s,%s,%s,%s)",(name,vno,model,no_of_owners,pre_owner,currentfuel,currenttype,insurance_renewal,owner_no,owner_addrs))
    address.commit()
    t.destroy()


    

def clr():
    """   global e
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9"""
    
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.set(fuel[1])
    e7.set(type[0])
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)


def func():
    t=Toplevel()
    t.title("New Registration")
    w=t.winfo_screenwidth()
    h=t.winfo_screenheight()
    t.geometry(f'{w}x{h}')
    t.resizable(False,False)
    f1=LabelFrame(t,text="New Registration!",padx=150,pady=150)
    f1.pack(padx=40,pady=40)

    b_n1=Label(f1,text="Name: ",width=50)
    b_n1.grid(row=0,column=0,padx=10,pady=10)

    global e
    e=StringVar()
    e=Entry(f1,width=50)
    e.grid(row=0,column=1,columnspan=2,padx=10,pady=10)

    b_n2=Label(f1,text="Vehicle Number: ",width=50)
    b_n2.grid(row=1,column=0,padx=10,pady=10)

    global e1
    e1=StringVar()
    e1=Entry(f1,width=50)
    e1.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

    b_n3=Label(f1,text="Model: ",width=50)
    b_n3.grid(row=2,column=0,padx=10,pady=10)

    global e2
    e2=StringVar()
    e2=Entry(f1,width=50)
    e2.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

    b_n4=Label(f1,text="No. of owners: ",width=50)
    b_n4.grid(row=3,column=0,padx=10,pady=10)

    global e3
    e3=StringVar()
    e3=Entry(f1,width=50)
    e3.grid(row=3,column=1,columnspan=2,padx=10,pady=10)

    b_n5=Label(f1,text="Pre-owners: ",width=50)
    b_n5.grid(row=4,column=0,padx=10,pady=10)

    global e4
    e4=StringVar()
    e4=Entry(f1,width=50)
    e4.grid(row=4,column=1,columnspan=2,padx=10,pady=10)

    b_n6=Label(f1,text="Current Owner: ",width=50)
    b_n6.grid(row=5,column=0,padx=10,pady=10)

    global e5
    e5=StringVar()
    e5=Entry(f1,width=50)
    e5.grid(row=5,column=1,columnspan=2,padx=10,pady=10)

    b_n7=Label(f1,text="Fuel: ",width=50)
    b_n7.grid(row=6,column=0,padx=10,pady=10)

    global e6
    global fuel
    fuel=[f'{9*"    "}Diesel{9*"    "}',f'{9*"    "}Petrol{9*"    "}',f'{8*"    "}Electrical{8*"    "}']
    e6=StringVar(value=fuel[1])
    option=OptionMenu(f1,e6,*fuel)
    option.grid(row=6,column=1,columnspan=2,padx=10,pady=10)

    b_n8=Label(f1,text="Type: ",width=50)
    b_n8.grid(row=7,column=0,padx=10,pady=10)

    global e7
    global type 
    type=[f'{9*"    "}Auto{9*"    "}',f'{9*"    "}Manual{9*"    "}']
    e7=StringVar(value=type[0])
    option2=OptionMenu(f1,e7,*type)
    option2.grid(row=7,column=1,columnspan=2,padx=10,pady=10)

    b_n9=Label(f1,text="Insurance Renewal: ",width=50)
    b_n9.grid(row=8,column=0,padx=10,pady=10)

    global e8
    e8=StringVar()
    e8=Entry(f1,width=50)
    e8.grid(row=8,column=1,columnspan=2,padx=10,pady=10)

    b_n10=Label(f1,text="Owner's phone number: ",width=50)
    b_n10.grid(row=9,column=0,padx=10,pady=10)

    global e9
    e9=StringVar()
    e9=Entry(f1,width=50)
    e9.grid(row=9,column=1,columnspan=2,padx=10,pady=10)

    b_n11=Label(f1,text="Owner's Address: ",width=50)
    b_n11.grid(row=10,column=0,padx=10,pady=10)

    global e10
    e10=StringVar()
    e10=Entry(f1,width=50)
    e10.grid(row=10,column=1,columnspan=2,padx=10,pady=10)

    b_clr=Button(f1,text='Clear',command=clr).grid(row=12,column=1,padx=10,pady=10)
    b_sum=Button(f1,text='Submit',command=lambda : sub(t)).grid(row=12,column=2,padx=10,pady=10)
   # b_back=Button(f1,text="Back",width=10,command=t.destroy).grid(padx=10,pady=10)




