from tkinter import *
from tkinter import messagebox
import mysql.connector
import ttkbootstrap as ttk



def showdetails(vdata):
    root=Tk()
    name=vdata[1]
    vehicle=vdata[2]
    model=vdata[3]
    pre_owners=vdata[5]
    current=vdata[1]
    fuel=vdata[6]
    types=vdata[7]
    ins=vdata[8]
    own_num=vdata[9]
    own_addrs=vdata[10]
    no_of_owners=vdata[4]

    f1=LabelFrame(root,text="Details",padx=150,pady=150)
    f1.grid(padx=40,pady=40)

    b_n1=Label(f1,text="Name : ",width=20)
    b_n1.grid(row=0,column=0,padx=10,pady=10)
    name1=Label(f1,text=name,width=50).grid(row=0,column=1)

    b_n2=Label(f1,text="Vehicle Number : ",width=15)
    b_n2.grid(row=1,column=0,padx=10,pady=10)
    veh1=Label(f1,text=vehicle,width=50).grid(row=1,column=1)

    b_n3=Label(f1,text="Model: ",width=10)
    b_n3.grid(row=2,column=0,padx=10,pady=10)
    mod=Label(f1,text=model,width=10).grid(row=2,column=1)

    b_n4=Label(f1,text="No. of owners: ",width=50)
    b_n4.grid(row=3,column=0,padx=10,pady=10)
    no_owners=Label(f1,text=no_of_owners,width=10).grid(row=3,column=1)

    b_n5=Label(f1,text="Pre-owners: ",width=50)
    b_n5.grid(row=4,column=0,padx=10,pady=10)
    pre_own=Label(f1,text=pre_owners,width=50).grid(row=4,column=1)

    b_n6=Label(f1,text="Current Owner: ",width=50)
    b_n6.grid(row=5,column=0,padx=10,pady=10)
    cowner=Label(f1,text=current,width=20).grid(row=5,column=1)

    b_n7=Label(f1,text="Fuel: ",width=50)
    b_n7.grid(row=6,column=0,padx=10,pady=10)
    fuel1=Label(f1,text=fuel,width=10).grid(row=6,column=1)

    b_n8=Label(f1,text="Type: ",width=50)
    b_n8.grid(row=7,column=0,padx=10,pady=10)
    typ=Label(f1,text=types,width=10).grid(row=7,column=1)

    b_n9=Label(f1,text="Insurance Renewal: ",width=50)
    b_n9.grid(row=8,column=0,padx=10,pady=10)
    ins1=Label(f1,text=ins,width=5).grid(row=8,column=1)

    b_n10=Label(f1,text="Owner's phone number: ",width=50)
    b_n10.grid(row=9,column=0,padx=10,pady=10)
    own_num1=Label(f1,text=own_num,width=12).grid(row=9,column=1)

    b_n11=Label(f1,text="Owner's Address: ",width=50)
    b_n11.grid(row=10,column=0,padx=10,pady=10)
    own_add=Label(f1,text=own_addrs,width=40).grid(row=10,column=1)


    


address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
mycursor=address.cursor()
mycursor.execute('select * from maintable')
data=[x for x in mycursor]
vehiclenos=[]
for i in data:
    vehiclenos.append(i[2])


def getNumber():
    root=Tk()
    root.title("Entry Field")

    def submit():
        sub1=value.get()
        root.destroy()
        print(sub1)
        if(sub1 in vehiclenos):
            showdetails(data[vehiclenos.index(sub1)])
        else:
            messagebox.showerror("Invalid Number",f'{sub1} is not registered yet !')

        
    root.geometry("600x450")
    lab=Label(root,text="VEHICLE NUMBER: ",width=20).grid(row=0,column=0,padx=40,pady=(200,40))

    global value
    v_no=StringVar(value='TN00*0000')
    value=ttk.Entry(root,textvariable=v_no,width=25)
    value.grid(row=0,column=1,columnspan=2,pady=(200,40))

    sub=Button(root,text="SUBMIT",width=20,command=submit)
    sub.grid(row=1,column=1,columnspan=2)


    root.mainloop()
