#from tkinter import _Cursor
import pyodbc
#Define connection to the Server and Database
connection =pyodbc.connect('Driver={SQL Server};'
             'Server=DESKTOP-2356QSV\SQLEXPRESS;'
             'Database=Food_Bev;'
             'Trusted_Connection=yes;')

#A Function to view all the data in my db

def view():
    cursor = connection.cursor()
    cursor.execute('SELECT Product.ProductDesc, Process.ProcessDesc, Temperature.[Temperature in Degrees celcuis], Pressure.Pressure, ERP.[ERP system], MES.[MES System] FROM ERP INNER JOIN ProductProcess ON ERP.ERP_ID = ProductProcess.ERP INNER JOIN MES ON ProductProcess.MES = MES.MES_ID INNER JOIN Process ON ProductProcess.ProcessID = Process.ProcessID INNER JOIN Product ON ProductProcess.ProductID = Product.ProductId INNER JOIN Pressure ON ProductProcess.PressureID = Pressure.Pressure_Id INNER JOIN Temperature ON ProductProcess.TemperatureID = Temperature.TemperatureId')
    rows = cursor.fetchall()  #Fetch the data from your db to be used by the program - use the fetchall() method
    #connection.close()
    return rows

def search(ProductDesc="", ProcessDesc=""):
    cursor = connection.cursor()
    cursor.execute('SELECT Product.ProductDesc, Process.ProcessDesc, Temperature.[Temperature in Degrees celcuis], Pressure.Pressure, ERP.[ERP system], MES.[MES System] FROM ERP INNER JOIN ProductProcess ON ERP.ERP_ID = ProductProcess.ERP INNER JOIN MES ON ProductProcess.MES = MES.MES_ID INNER JOIN Process ON ProductProcess.ProcessID = Process.ProcessID INNER JOIN Product ON ProductProcess.ProductID = Product.ProductId INNER JOIN Pressure ON ProductProcess.PressureID = Pressure.Pressure_Id INNER JOIN Temperature ON ProductProcess.TemperatureID = Temperature.TemperatureId WHERE ProductDesc=? OR ProcessDesc=?', (ProductDesc,ProcessDesc))
    rows = cursor.fetchall()  #Fetch the data from your db to be used by the program - use the fetchall() method
   # connection.close()
    return rows
    

#print(view())
#print(search(ProductDesc="Milk"))
              