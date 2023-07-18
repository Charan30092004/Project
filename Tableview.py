from tkinter import *
from tkinter import ttk
import mysql.connector

root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry(f'{w}x{h}')
root.title("Vehicle Data ")





def tableshow(data):

    mainframe=Frame(root)
    mainframe.pack(fill=BOTH,expand=1)

    
    my_canvas=Canvas(mainframe)

    hr=Scrollbar(mainframe,orient=HORIZONTAL,width=20,command=my_canvas.xview)
    hr.pack(fill=X)
   
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    vr=Scrollbar(mainframe,orient=VERTICAL,width=20  ,command=my_canvas.yview)
    vr.pack(side=RIGHT,fill=Y)

    my_canvas.config(yscrollcommand=vr.set)
    my_canvas.bind('<Configure>', lambda event:my_canvas.configure(scrollregion=my_canvas.bbox('all'))) 
    
    my_canvas.config(xscrollcommand=hr.set)
    my_canvas.bind('<Configure>', lambda event:my_canvas.configure(scrollregion=my_canvas.bbox('all')))   

    second_frame=Frame(my_canvas)

    my_canvas.create_window((0,0),window=second_frame,anchor='nw')


    table=ttk.Treeview(second_frame,columns=('s.no','no','currentowner','model','fuel','ownerNumber','type','address','insurance','NumberofOwner'),show='headings')
    table.pack()
    table.heading("s.no",text="Serial Number")
    table.heading("no",text="Vehicle Number")
    table.heading("currentowner",text="Owner")
    table.heading("model",text="Vehicle Model")
    table.heading('fuel',text="Fuel")
    table.heading("ownerNumber",text="Owner Phone")
    table.heading('type',text="Vehicle Type")
    table.heading("address",text="Owner Address")
    table.heading('insurance',text="Insurance Renewal Date")
    table.heading("NumberofOwner",text="Number of owners")


    i=1
    for x in data:
        value=(i,x[2],x[1],x[3],x[6],x[9],x[7],x[10],x[8],x[4])
        i+=1
        table.insert(parent='',index=-1,values=value)



def tableview(tn):
    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
    mycursor=address.cursor()
    mycursor.execute('select * from maintable')
    data=[x for x in mycursor if x[2][:4]==tn]
    print(data)
    tableshow(data)




root.mainloop()