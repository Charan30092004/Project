from tkinter import *
root=Tk()

def func():
    t=Toplevel()
    f1=LabelFrame(t,text="New Registration!",padx=150,pady=150)
    f1.pack(padx=40,pady=40)
    b_n1=Label(f1,text="Name: ",width=50)
    b_n1.grid(row=0,column=0,padx=10,pady=10)
    e=Entry(f1,width=50)
    e.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
    b_n2=Label(f1,text="Vehicle Number: ",width=50)
    b_n2.grid(row=1,column=0,padx=10,pady=10)
    e1=Entry(f1,width=50)
    e1.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
    b_n3=Label(f1,text="Model: ",width=50)
    b_n3.grid(row=2,column=0,padx=10,pady=10)
    e2=Entry(f1,width=50)
    e2.grid(row=2,column=1,columnspan=2,padx=10,pady=10)
    b_n4=Label(f1,text="No. of owners: ",width=50)
    b_n4.grid(row=3,column=0,padx=10,pady=10)
    e3=Entry(f1,width=50)
    e3.grid(row=3,column=1,columnspan=2,padx=10,pady=10)
    b_n5=Label(f1,text="Pre-owners: ",width=50)
    b_n5.grid(row=4,column=0,padx=10,pady=10)
    e4=Entry(f1,width=50)
    e4.grid(row=4,column=1,columnspan=2,padx=10,pady=10)
    b_n6=Label(f1,text="Current Owner: ",width=50)
    b_n6.grid(row=5,column=0,padx=10,pady=10)
    e5=Entry(f1,width=50)
    e5.grid(row=5,column=1,columnspan=2,padx=10,pady=10)
    b_n7=Label(f1,text="Fuel: ",width=50)
    b_n7.grid(row=6,column=0,padx=10,pady=10)
    e6=Entry(f1,width=50)
    e6.grid(row=6,column=1,columnspan=2,padx=10,pady=10)
    b_n8=Label(f1,text="Type: ",width=50)
    b_n8.grid(row=7,column=0,padx=10,pady=10)
    e7=Entry(f1,width=50)
    e7.grid(row=7,column=1,columnspan=2,padx=10,pady=10)
    b_n9=Label(f1,text="Insurance Renewal: ",width=50)
    b_n9.grid(row=8,column=0,padx=10,pady=10)
    e8=Entry(f1,width=50)
    e8.grid(row=8,column=1,columnspan=2,padx=10,pady=10)
    b_n10=Label(f1,text="Owner's phone number: ",width=50)
    b_n10.grid(row=9,column=0,padx=10,pady=10)
    e9=Entry(f1,width=50)
    e9.grid(row=9,column=1,columnspan=2,padx=10,pady=10)
    b_n10=Label(f1,text="Owner's Address: ",width=50)
    b_n10.grid(row=10,column=0,padx=10,pady=10)
    e9=Entry(f1,width=50)
    e9.grid(row=10,column=1,columnspan=2,padx=10,pady=10)
    b_clr=Button(f1,text='Clear').grid(row=12,column=1,padx=10,pady=10)
    b_sum=Button(f1,text='Submit').grid(row=12,column=2,padx=10,pady=10)
   # b_back=Button(f1,text="Back",width=10,command=t.destroy).grid(padx=10,pady=10)


btn=Button(root,text="click",width=10,command=func).grid(padx=10,pady=10)
root.mainloop()