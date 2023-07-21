import matplotlib.pyplot as plt
import mysql.connector


def graph(userid):
    address=mysql.connector.connect(host="localhost",user="root",passwd="Charan@2023",database="Python")
    mycursor=address.cursor()
    mycursor.execute('select * from maintable')
    data=[x[6] for x in mycursor if x[2][:4]==userid]
    x=data.count("Petrol")
    y=data.count("Diesel")
    z=data.count("Electrical")
    label = 'PETROL', 'DIESEL', 'EV'
    sizes = [x,y,z]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=label)
    plt.title("FUEL CHART")
    plt.show()
