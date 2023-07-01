from tkinter import *
import mysql.connector
from tkinter import messagebox
address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="python")
mycursor=address.cursor()

root=Tk()
root.title("Offical Login")
userid_value="TN01"



root.mainloop()