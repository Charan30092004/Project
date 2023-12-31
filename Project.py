
from tkinter import *
import ttkbootstrap as ttk
import Personal as P
from PIL import Image,ImageTk
import mysql.connector
from Tableview import *
from personalview import *
from tkinter import messagebox
from updatedetails import *
from chart import *

from userdetails import *
from AdditionalFunctions import checkPhoneNumber
root=ttk.Window(themename="superhero")#superhero#litera#darkly
#root=Tk()


def personalWindow():
    global firstpage
    firstpage.destroy()
    root.title("Personal Access")

    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()

    root.geometry(f'{w//2}x{h//2}')

    personalframe=LabelFrame(root,text="Personal Access",padx=60,pady=30)
    personalframe.grid(padx=w//5,pady=h//6)
    
    
    

    def personalLogin():

        #Database Connection
        address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="python")
        mycursor=address.cursor()

        mycursor.execute("select * from userdetails")
        userlogindetails=[x[3]for x in mycursor]
        mycursor.execute("select * from userdetails")
        passwdlogindetails=[x[5] for x in mycursor]
    
        login=Tk()
        login.title("Log in")
        login.geometry('300x200+100+100')
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
                    getNumber()
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



    login=Button(personalframe,text="LOG IN",padx=5,command=personalLogin)
    login.grid(padx=5,pady=5)

    signup=Button(personalframe,text="SIGN UP",padx=2,command=P.personalSignup)
    signup.grid(padx=5,pady=5)

    def goback():
        personalframe.destroy()
        OpenWindow()
    back=Button(personalframe,text="Back",padx=11,command=goback)
    back.grid(padx=5,pady=5)

def offical_login(index):

    #Database Connection
    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="python")
    mycursor=address.cursor()
    
    mycursor.execute(f'Select * From offical_details')
    offical_details=mycursor.fetchall()[index]
    userid_value=offical_details[1]

    #Back Button
    def backfun():
        offical_login_frame.destroy()
        OfficalWindow()
    

    #View profile Details
    def profilefun():
        offical_login_frame.destroy()
        profile_frame=LabelFrame(root,text="Profile Details",padx=20,pady=20)
        profile_frame.grid(padx=100,pady=(150,20))

        code=Label(profile_frame,text="Office Code : ").grid(row=0,column=0)
        codevalue=Label(profile_frame,text=offical_details[1]).grid(row=0,column=1,pady=10)

        name=Label(profile_frame,text="Office Name : ").grid(row=1,column=0)
        namevalue=Label(profile_frame,text=offical_details[2]).grid(row=1,column=1,pady=10)

        address=Label(profile_frame,text="Office Address : ").grid(row=2,column=0)
        addressvalue=Label(profile_frame,text=offical_details[3]).grid(row=2,column=1,pady=10)

        lanline=Label(profile_frame,text="Office Lanline : ").grid(row=3,column=0)
        lanlinevalue=Label(profile_frame,text=offical_details[4]).grid(row=3,column=1,pady=10)

        phone=Label(profile_frame,text="Office Cell : ").grid(row=4,column=0)
        phonevalue=Label(profile_frame,text=offical_details[5]).grid(row=4,column=1,pady=10)

        mail=Label(profile_frame,text="Offical Mail : ").grid(row=5,column=0)
        mailvalue=Label(profile_frame,text=offical_details[6]).grid(row=5,column=1)

        #Creating back and logout Button
        def backfun():
            profile_frame.destroy()
            offical_login(index)
        def logoutfun():
            profile_frame.destroy()
            OfficalWindow()
        
        back=Button(profile_frame,text="Back",padx=20,command=backfun)
        back.grid(row=6,column=1,pady=15)

        logout=Button(profile_frame,text="LOG OUT",padx=7,command=logoutfun)
        logout.grid(row=7,column=1)
    

    #View Details
    def viewdetails(userid_value):

        #back button
        def backfun():
            viewdetails_frame.destroy()
            offical_login(index)

        #logout button
        def logoutfun():
            viewdetails_frame.destroy()
            OfficalWindow()



        offical_login_frame.destroy()

        viewdetails_frame=LabelFrame(root,text=f'View Details of {userid_value}',padx=40,pady=40)
        viewdetails_frame.grid(padx=300,pady=150)

        table=Button(viewdetails_frame,text="Tables",padx=18,command=lambda : tableview(userid_value))
        table.grid(row=0,column=0,padx=20,pady=15)

        chart=Button(viewdetails_frame,text="Chart",padx=20,command= lambda : graph(userid_value))
        chart.grid(row=1,column=0,padx=20,pady=15)

        back=Button(viewdetails_frame,text="Back",padx=22,command=backfun)
        back.grid(row=2,column=0,padx=20,pady=15)

        logout=Button(viewdetails_frame,text="LOG OUT",padx=10,command=logoutfun)
        logout.grid(row=3,column=0,padx=20,pady=15)





    #UpdateFrame
    def UpdateDetails(userid_value):
        offical_login_frame.destroy()
        

        #back button
        def backfun():
            update_frame.destroy()
            offical_login(index)

        #logout button
        def logoutfun():
            update_frame.destroy()
            OfficalWindow()

        update_frame=LabelFrame(root,text="Update Records",padx=40,pady=40)
        update_frame.grid(padx=300,pady=150)

        add=Button(update_frame,text="New Record",padx=7,command=func)
        add.grid(row=0,column=0,padx=20,pady=15)


        def updatecallingfunction():
            update_frame.destroy()
            updatefunction(userid_value,root)

        edit=Button(update_frame,text="Edit Record",padx=10,command= updatecallingfunction)
        edit.grid(row=1,column=0,padx=20,pady=15)

        back=Button(update_frame,text="Back",padx=26,command=backfun)
        back.grid(row=2,column=0,padx=20,pady=15)

        logout=Button(update_frame,text="LOG OUT",padx=15,command=logoutfun)
        logout.grid(row=3,column=0,padx=20,pady=15)




    Officalframe.destroy()
    offical_login_frame=LabelFrame(root,text=userid_value,padx=40,pady=20)
    offical_login_frame.grid(padx=300,pady=200)

    view=Button(offical_login_frame,text="View Details",padx=7.5,pady=5,command=lambda : viewdetails(userid_value))
    view.grid(row=0,column=0,padx=20,pady=10)

    update=Button(offical_login_frame,text="Update",padx=20,pady=5,command= lambda :UpdateDetails(userid_value))
    update.grid(row=1,column=0,padx=20,pady=10)

    profile=Button(offical_login_frame,text="View Profile",padx=8,pady=5,command=profilefun)
    profile.grid(row=2,column=0,padx=20,pady=10)

    back=Button(offical_login_frame,text="Back",padx=26,pady=5,command=backfun)
    back.grid(row=3,column=0,padx=20,pady=10)





def OfficalWindow():

    #Database Connection
    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="python")
    mycursor=address.cursor()

    #gathering userid details from the database
    mycursor.execute("SELECT * FROM offical_details")
    userid_values=[x[1] for x in mycursor]

    #gathering password details from the database
    mycursor.execute("SELECT * From offical_details")
    passwd_values=[x[7] for x in mycursor]


    global firstpage
    firstpage.destroy()
    root.title("Offical Access")

    global Officalframe
    Officalframe=LabelFrame(root,text="Offical Login",padx=50,pady=30)
    Officalframe.grid(padx=250,pady=175)

    useridlb=Label(Officalframe,text="User id : ")
    useridlb.grid(row=0,column=0,padx=(20,0))

    global userid
    userid=StringVar()
    userid=Entry(Officalframe)
    userid.grid(row=0,column=1,columnspan=2,pady=10)

    passwdlb=Label(Officalframe,text="Password : ")
    passwdlb.grid(row=1,column=0,padx=(20,0))

    global passwd
    passwd=StringVar()
    passwd=Entry(Officalframe)
    passwd.grid(row=1,column=1,columnspan=2,pady=10)


    def goback():
        Officalframe.destroy()
        OpenWindow()
    back=Button(Officalframe,text="Back",padx=6,command=goback)
    back.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

    

    def clearfun():
        global userid
        global passwd

        userid.delete(0,END)
        passwd.delete(0,END)

    clear=Button(Officalframe,text="Clear",command=clearfun)
    clear.grid(row=2,column=1,padx=5,pady=(10,5))

    def checklogin():
        userid_value=userid.get()
        passwd_value=passwd.get()
        clearfun()
        if (userid_value in userid_values):
            index=userid_values.index(userid_value)
            if(passwd_values[index]==passwd_value):
                offical_login(index)
            else:
                messagebox.showwarning("Access Denied","You have Entered a Wrong Password")
        else:
            messagebox.showwarning("Wrong Details","User Name not Found")
        


    submit=Button(Officalframe,text="Submit",command=checklogin)
    submit.grid(row=2,column=2,padx=5,pady=5)


#openin page of the Application 

def OpenWindow():

    root.geometry('800x600+100+100')
    root.resizable(False,False)
    root.title("RTO Manager")

    global firstpage
    firstpage=LabelFrame(root,text="Role",padx=50,pady=30)
    firstpage.grid(padx=300,pady=200)

    personal=Button(firstpage,text="Personal",padx=5,pady=5,command=personalWindow)
    personal.grid(row=0,column=0,padx=10,pady=10)


    offical=Button(firstpage,text="Offical",padx=10,pady=5,command=OfficalWindow)
    offical.grid(row=1,column=0,padx=10,pady=10)

#first statement to run the application
OpenWindow()



root.mainloop()