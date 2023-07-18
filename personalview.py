from tkinter import *
root=Tk()
name="hari"
vehicle="mini"
model="a6"
pre_owners="hvg hbhb"
current="dssf"
fuel="petrol"
types="manual"
ins=2006
own_num=43632
own_addrs="ds dfv"
no_of_owners=3
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


root.mainloop()