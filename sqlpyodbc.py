
'''import pyodbc
import pandas.io.sql as psql
cnxn=pyodbc.connect(DRIVER='{SQL Server}',server='DESKTOP-UKA5IHV',database='jaswanth',trustedconnection='yes')
cursor=cnxn.cursor()
cursor.execute("use jaswanth")
sql="select * from emp"
df=psql.read_sql_query(sql,cnxn)
print(df)
cnxn.close()
'''
'''
import pyodbc
import pandas.io.sql as psql
cnxn=pyodbc.connect(DRIVER='{SQL Server}',server='DESKTOP-UKA5IHV',database='jaswanth',trustedconnection='yes')
cursor=cnxn.cursor()
cursor.execute('use jaswanth')
v='update EMP set COMM=100 where EMPNO=7369'
cursor.execute(v)
cursor.execute('COMMIT')
print("Updated Successfully")
print(cursor.rowcount," rows are effected")
cnxn.close()
'''
from tkinter import *
import pyodbc
import pandas.io.sql as psql

root = Tk()
root.title("Dept List")


label1 =Label(root, text ="Deptno")
label1.grid(row =1, column =0)

num1_txtbx =Entry(root)
num1_txtbx.grid(row =1, column =1)

label2 =Label(root, text ="Dname")
label2.grid(row =2, column =0)

num2_txtbx =Entry(root)
num2_txtbx.grid(row =2, column =1)

label3 =Label(root, text ="Loc")
label3.grid(row =3, column =0)

num3_txtbx =Entry(root)
num3_txtbx.grid(row =3, column =1)


def Result():
    cnxn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',server = 'DESKTOP-9AOCNUU',database='python',Trusted_Connection='yes')
    cursor = cnxn.cursor()
    cursor.execute("use python")
    m1=int(num1_txtbx.get())
    m2=num2_txtbx.get()
    m3=num3_txtbx.get()
    print ("insert into dept(deptno,dname,loc) values("+str(m1)+','+"'"+m2+"'"+','+"'"+m3+"'"+")")
    cursor.execute("insert into dept(deptno,dname,loc) values("+str(m1)+','+"'"+m2+"'"+','+"'"+m3+"'"+")")
    cursor.commit();
    print ('1 row inserted')
    cnxn.close();
    
calculate_button =Button(root, text="Insert", command= Result)
calculate_button.grid(row =4, column =0,columnspan=2)


root.mainloop()



  
