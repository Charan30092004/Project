from tkinter import *
import Personal as P
import mysql
from tkinter import messagebox
from AdditionalFunctions import checkPhoneNumber
root=Tk()


def personalWindow():
    global firstpage
    firstpage.destroy()
    root.title("Personal Access")

    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()

    root.geometry(f'{w//2}x{h//2}')

    personalframe=LabelFrame(root,text="Personal Access",padx=60,pady=30)
    personalframe.grid(padx=w//5,pady=h//6)


    login=Button(personalframe,text="LOG IN",padx=5,command=P.personalLogin)
    login.grid(padx=5,pady=5)

    signup=Button(personalframe,text="SIGN UP",padx=2,command=P.personalSignup)
    signup.grid(padx=5,pady=5)

    def goback():
        personalframe.destroy()
        OpenWindow()
    back=Button(personalframe,text="Back",padx=6,command=goback)
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





    Officalframe.destroy()
    offical_login_frame=LabelFrame(root,text=userid_value,padx=40,pady=20)
    offical_login_frame.grid(padx=300,pady=200)

    view=Button(offical_login_frame,text="View Details",padx=7.5,pady=5)
    view.grid(row=0,column=0,padx=20,pady=10)

    update=Button(offical_login_frame,text="Update",padx=20,pady=5)
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

OpenWindow()



root.mainloop()