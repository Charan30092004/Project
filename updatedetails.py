from tkinter import *
from tkinter import messagebox
import mysql.connector
import ttkbootstrap as bs
#root=Tk()
#root.geometry()


def reload():
    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
    mycursor=address.cursor()
    mycursor.execute('select * from maintable')
    data=[x for x in mycursor if x[2][:4]==c]
    currentNumber=e.get()
    vehicleNumber=[x[2] for x in data]
    index=vehicleNumber.index(currentNumber)
    details=data[index]
    name.set(details[1])
    vehicle.set(details[2])
    model.set(details[3])
    no_of_owners.set(details[4])
    pre_owners.set(details[5])
    fuel.set(details[6])
    types.set(details[7])
    ins.set(details[8])
    own_num.set(details[9])
    own_addrs.set(details[10])
       
    


def func(data,root):
    
    root.geometry("900x900+100+100")

    vehicleNumber=[x[2] for x in data]
    currentNumber=e.get()
    if(currentNumber in vehicleNumber):
        index=vehicleNumber.index(currentNumber)
        details=data[index]
        serialnumber=details[0]
    else:
        messagebox.showerror("Invalid Number",f'{currentNumber} is not Registered Yet ! ')
        return
    

    global name,vehicle,model,no_of_owners,pre_owners,fuel,types,ins,own_num,own_addrs
    name=StringVar()
    vehicle=StringVar()
    model=StringVar()
    no_of_owners=IntVar()
    pre_owners=StringVar()
    fuel=StringVar()
    types=StringVar()
    ins=StringVar()
    own_num=StringVar()
    own_addrs=StringVar()


    def editdetails():
        n=name.get()
        v=vehicle.get()
        m=model.get()
        no=no_of_owners.get()
        po=pre_owners.get()
        f=fuel.get()
        t=types.get()
        i=ins.get()
        on=own_num.get()
        oa=own_addrs.get()
        print(name.get())

        address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
        mycursor=address.cursor()
        """query= f'UPDATE  SET `Name` = `{n}`, `Vehicle Model` = `{m}`, `Number of Owner` = `{no}`, `Previous Owner` = `{po}`, `Fuel` = `{f}`, `Type` =`{t}`, `Insurance` =`{i}`, `Owner Mobile Number` = `{on}`, `Owner Address` = `{oa}` WHERE (`S.No` = `{serialnumber}`)' 
                                                                                                                                                                                                                                                    value=(n,m,no,po,f,t,i,on,oa,serialnumber)
        mycursor.execute(query)"""
        mycursor.execute("DELETE FROM `maintable` WHERE (`S.No` = %s)",(serialnumber,))
        address.commit()
        mycursor.execute("INSERT INTO `maintable` (`S.No`, `Name`, `VehicleNumber`, `Vehicle Model`, `Number of Owner`, `Previous Owner`, `Fuel`, `Type`, `Insurance`, `Owner Mobile Number`, `Owner Address`) VALUES ( %s,%s, %s, %s, %s,%s, %s, %s,%s,%s,%s)",(serialnumber,n,v,m,no,po,f,t,i,on,oa))
        address.commit()
        reload()




       
    '''name=details[1]
    vehicle=details[2]
    model=details[3]
    no_of_owners=details[4]
    pre_owners=details[5]
    fuel=details[6]
    types=details[7]
    ins=details[8]
    own_num=details[9]
    own_addrs=details[10]'''


    def resetdetails():
        name.set(details[1])
    
        vehicle.set(details[2])
        model.set(details[3])
        no_of_owners.set(details[4])
        pre_owners.set(details[5])
        fuel.set(details[6])
        types.set(details[7])
        ins.set(details[8])
        own_num.set(details[9])
        own_addrs.set(details[10])
        reload()
    resetdetails()


    f1=LabelFrame(root,text="Details",padx=50,pady=25)
    f1.grid(padx=40,pady=40,row=3,column=0,columnspan=2)

    b_n1=Label(f1,text="Name : ",width=20)
    b_n1.grid(row=0,column=0,padx=10,pady=10)
    name1=bs.Entry(f1,textvariable=name,width=30)
    name1.grid(row=0,column=1,columnspan=2)
    #name1.insert(name)

    b_n2=Label(f1,text="Vehicle Number : ",width=15)
    b_n2.grid(row=1,column=0,padx=10,pady=10)
    veh1=bs.Entry(f1,textvariable=vehicle,width=30)
    veh1.grid(row=1,column=1,columnspan=2)
    veh1.config(state=DISABLED)
    #veh1.insert(vehicle)

    b_n3=Label(f1,text="Model: ",width=10)
    b_n3.grid(row=2,column=0,padx=10,pady=10)
    mod=bs.Entry(f1,textvariable=model,width=30)
    mod.grid(row=2,column=1,columnspan=2)
    #mod.insert("model")

    b_n4=Label(f1,text="No. of owners: ",width=50)
    b_n4.grid(row=3,column=0,padx=10,pady=10)
    no_owners=bs.Entry(f1,textvariable=no_of_owners,width=30)
    no_owners.grid(row=3,column=1,columnspan=2)
    #no_owners.insert(no_of_owners)

    b_n5=Label(f1,text="Pre-owners: ",width=50)
    b_n5.grid(row=4,column=0,padx=10,pady=10)
    pre_own=bs.Entry(f1,textvariable=pre_owners,width=30)
    pre_own.grid(row=4,column=1,columnspan=2)
        #pre_own.insert(pre_owners)

    b_n7=Label(f1,text="Fuel: ",width=50)
    b_n7.grid(row=6,column=0,padx=10,pady=10)
    fuel1=bs.Entry(f1,textvariable=fuel,width=30)
    fuel1.grid(row=6,column=1,columnspan=2)
        #fuel1.insert(fuel)

    b_n8=Label(f1,text="Type: ",width=50)
    b_n8.grid(row=7,column=0,padx=10,pady=10)
    typ=bs.Entry(f1,textvariable=types,width=30)
    typ.grid(row=7,column=1,columnspan=2)
        #typ.insert(types)

    b_n9=Label(f1,text="Insurance Renewal: ",width=50)
    b_n9.grid(row=8,column=0,padx=10,pady=10)
    ins1=bs.Entry(f1,textvariable=ins,width=30)
    ins1.grid(row=8,column=1,columnspan=2)
        #ins1.insert(ins)

    b_n10=Label(f1,text="Owner's phone number: ",width=50)
    b_n10.grid(row=9,column=0,padx=10,pady=10)
    own_num1=bs.Entry(f1,textvariable=own_num,width=30)
    own_num1.grid(row=9,column=1,columnspan=2)
        #own_num1.insert(own_num)
        

    b_n11=Label(f1,text="Owner's Address: ",width=50)
    b_n11.grid(row=10,column=0,padx=10,pady=10)
    own_add=bs.Entry(f1,textvariable=own_addrs,width=30)
    own_add.grid(row=10,column=1,columnspan=2)
        #own_add.insert(own_addrs)



    reset=Button(f1,text="RESET",command=resetdetails)
    reset.grid(padx=40,pady=10,row=11,column=1)
    save=Button(f1,text="SAVE",command=editdetails)
    save.grid(padx=40,pady=10,row=11,column=2)
    




def updatefunction(code,rootvalue):
    global c,root
    c=code
    root=rootvalue
    root.geometry("400x200+150+150")
    #root=bs.Window(themename="superhero")
    lab=Label(root,text="Vehicle Number: ",width=20)
    lab.grid(padx=10,pady=50,row=0,column=0)
    
    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
    mycursor=address.cursor()
    mycursor.execute('select * from maintable')
    data=[x for x in mycursor if x[2][:4]==code]

    print(data)

    global e
    e=bs.Entry(root,width=20)
    e.grid(row=0,column=1,padx=20)



    btn=Button(root,text="Get Details ",command=lambda : func(data,root))
    btn.grid(padx=10,pady=10,row=2,column=1)

    root.mainloop()

#updatefunction("TN52",bs.Window(themename="superhero"))
