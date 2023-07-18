#build in modules
from tkinter import *
import mysql.connector
from tkinter import messagebox


#user Defined Modules
from AdditionalFunctions import checkPhoneNumber
from AdditionalFunctions import checkpassword

#Database Connection
address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="python")
mycursor=address.cursor()

"""def personalLogin():

    mycursor.execute("select * from userdetails")
    userlogindetails=[x[3]for x in mycursor]
    mycursor.execute("select * from userdetails")
    passwdlogindetails=[x[5] for x in mycursor]
    
    login=Tk()
    login.title("Log in")
    login.geometry('250x200+100+100')
    login.resizable(False,False)

    useridlb=Label(login,text="User id : ")
    useridlb.grid(row=0,column=0,padx=(20,0))

    global userid
    userid=StringVar()
    userid=Entry(login)
    userid.grid(row=0,column=1,pady=10,columnspan=2)

    passwdlb=Label(login,text="Password : ")
    passwdlb.grid(row=1,column=0,padx=(20,0))

    global passwd
    passwd=StringVar()
    passwd=Entry(login)
    passwd.grid(row=1,column=1,pady=10,columnspan=2)

    def getdetails():
        global userid
        global passwd
        useridvalue=userid.get()
        passwdvalue=passwd.get()
        
        login.destroy()
        if(useridvalue in userlogindetails):
            index=userlogindetails.index(useridvalue)
            if(passwdvalue == passwdlogindetails[index]):
                return True
            else:
                messagebox.showerror("Access Denied","Entered a Wrong Password")
        else:
            messagebox.showerror("Wrong Detail","User Name Not Found")

    def clearfun():
        global userid
        global passwd

        userid.delete(0,END)
        passwd.delete(0,END)

    submit=Button(login,text="Submit",command=getdetails)
    clear=Button(login,text="Clear",command=clearfun)
    submit.grid(row=2,column=1,pady=20,padx=20)
    clear.grid(row=2,column=2)
"""
def personalSignup():

    def clearfun():
        global name
        global phone
        global userId
        global password
        global dob

        name.delete(0,END)
        phone.delete(0,END)
        userId.delete(0,END)
        password.delete(0,END)
        dob.delete(0,END)
    
    def sumbitfun():
        global name
        global phone
        global userId
        global password
        global dob

        namevalue=name.get()
        phonevalue=phone.get()
        userIdvalue=userId.get()
        passwordvalue=password.get()
        dobvalue=dob.get()

        clearfun()

        mycursor.execute("select * from userdetails")
        userIds=[x[3] for x in mycursor]

        signup.destroy()

        if(userIdvalue in userIds):
            messagebox.showerror('Warning','User Name Already Exist')
        elif(not checkPhoneNumber(phonevalue)):
            messagebox.showerror("Warning","Phone Number Entered is not valid ! ")
        elif(not checkpassword(passwordvalue)):
            messagebox.showerror("Warning","Your Password should atleast contain \n1 Lowercase\n1 Uppercase \n1 Symbol \n1 NumericValue\n minimum length of 8")
        else:
            mycursor.execute("INSERT INTO `userdetails` (`Name`, `Phone Number`, `User Id`, `Date of Birth`, `Password`) VALUES (%s , %s, %s ,%s, %s)",(namevalue,phonevalue,userIdvalue,dobvalue,passwordvalue))
            address.commit()


        


    signup=Tk()
    signup.title("Sign Up")
    signup.geometry('350x300+100+100')
    signup.resizable(False,False)

    global name 
    name=StringVar()
    global phone
    phone=StringVar()
    global userId 
    userId=StringVar
    global password
    userId=StringVar()
    global dob 
    dob=StringVar()
    
    namelb=Label(signup,text="Name : ")
    name=Entry(signup)
    namelb.grid(row=0,column=0,padx=20,pady=10)
    name.grid(row=0,column=1,columnspan=2)

    userIdlb=Label(signup,text="User Id : ")
    userId=Entry(signup)
    userIdlb.grid(row=1,column=0,padx=20,pady=10)
    userId.grid(row=1,column=1,columnspan=2)

    passwordlb=Label(signup,text="Password : ")
    password=Entry(signup)
    passwordlb.grid(row=2,column=0,padx=20,pady=10)
    password.grid(row=2,column=1,columnspan=2)

    phonelb=Label(signup,text="Phone Number : ")
    phone=Entry(signup)
    phonelb.grid(row=3,column=0,padx=20,pady=10)
    phone.grid(row=3,column=1,columnspan=2)

    doblb=Label(signup,text="Date of Birth :")
    dob=Entry(signup)
    
    doblb.grid(row=4,column=0,padx=20,pady=10)
    dob.grid(row=4,column=1,columnspan=2)
    dob.insert(0,'YYYY-MM-DD')
    

    clear=Button(signup,text="Clear",command=clearfun)
    sumbit=Button(signup,text="Sumbit",command=sumbitfun)
    clear.grid(row=5,column=1,padx=20,pady=10)
    sumbit.grid(row=5,column=2,padx=20,pady=10)


    



