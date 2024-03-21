import pyodbc
import datetime 
import pandas.io.sql as psql
import pandas as pd
import sys
cnxn=pyodbc.connect(driver='{SQL Server}',server='DESKTOP-UKA5IHV',trustedconnection='yes')
cursor=cnxn.cursor()
class Bank:
    def AccountTable(self):
        cursor.execute("use jaswanth")
        insert='create table Bank(accno int primary key,cname nvarchar(40),balance int,city varchar(20),phonenumber bigint)'
        cursor.execute(insert)
        cursor.execute("commit")
        users = [
        (1001, 'Jaswanth',25000, 'Gachibowli',9059514677), 
        (1002, 'Lois',30000, 'KPHB',9837376772), 
        (1003, 'Peter',20000,'Boduppall',9922335544), 
        (1004, 'Bruce',53000,'Gotham',9848000123)
        ]
        cursor.executemany("insert into Bank values(?,?,?,?,?)",users)
        cursor.execute("commit")
        print("rows inserted")

    def InsertAccount(self):
        print("Hello! Welcome to Bank \n")
        print("Please Create your Account")
        try:
            self.accno=int(input("Enter Account Number :"))
            self.name=input("Enter Customer Name :")
            self.balance=int(input("Enter Account Balance :"))
            self.city=input("Enter City :")
            self.phonenumber=int(input("Enter Phone Number :"))
        except Exception:
            print("Please enter correct details")
        try:    
            cursor.execute("use jaswanth")
            cursor.execute("insert into bank values(?,?,?,?,?)",self.accno,self.name,self.balance,self.city,self.phonenumber)
            cursor.execute("commit")
            print("row inserted")
            print("Congratulations your account was created")
        except Exception:
            print("Something Wrong Please Try Again ")


    def DepositAmount(self):
        print("DEPOST AMUNT \n")
        self.accno=int(input("Enter Account No You want to Deposit :"))
        self.amount=int(input("Enter Amount :"))
        cursor.execute("use jaswanth")
        df=pd.read_sql_query("select * from BANK",cnxn)
        if ((df['accno']==self.accno)).any():
            cursor.execute('update BANK set balance+=? where accno=?',self.amount,self.accno)
            print(f'{ cursor.rowcount } effected')
            print("DEPOSITED SUCCESSFULLY")
            cursor.execute("commit")
        else:
            print("ACCOUNT DO NOT EXISTS")

    def WithdrawAmount(self):
        print("WITHDRAWAL \n")
        self.accno=int(input("Enter Account No You want to Withdraw :"))
        self.amount=int(input("Enter Amount :"))
        cursor.execute("use jaswanth")
        df=pd.read_sql_query("select * from BANK",cnxn)
        if ((df['accno']==self.accno)).any():
            cursor.execute("select balance from bank where accno=?",self.accno)
            bal=cursor.fetchone()
            if self.amount<=bal.balance:
                cursor.execute('update BANK set balance-=? where accno=?',self.amount,self.accno)
                cursor.execute("commit")
                print(f'{ cursor.rowcount } effected')
                print("WIHDRAW SUCCESSFULLY COMPLETED")
                
            else:
                print("INSUFFICIENT BALANCE")
        else:
            print("ACCOUNT DO NOT EXISTS")

    def BalanceEnquiry(self):
        print("BALANCE ENQUIRY \n")
        cursor.execute("use jaswanth")
        self.accno=int(input("Enter Acc No :"))
        cursor.execute("use jaswanth")
        sql="select * from bank"
        df=pd.read_sql_query(sql,cnxn)
        if ((df['accno']==self.accno)).any():
            bf=df.loc[df['accno']==self.accno]
            print("Balance Amount : ",bf.balance.values[0])
        else:
            print("ACCOUNT DO NOT EXISTS")

    def PrintAccounts(self):
        print("ALL ACCOUNTS LIST \n")
        cursor.execute("use jaswanth")
        df=pd.read_sql_query("select * from bank",cnxn)
        print(df.to_string(index=False))

    def CloseAccount(self):
        self.accno=int(input("Enter ACC NO of the Account you want to delete: "))
        cursor.execute("use jaswanth")
        df=pd.read_sql_query("select * from bank",cnxn)
        if ((df['accno']==self.accno)).any():
            cursor.execute("delete from bank where accno=?",self.accno)
            cursor.execute("commit")
            print(f'{cursor.rowcount} row affected')
        else:
            print("ACCOUNT DO NOT EXISTS")

    def ModifyAccount(self):
        self.accno=(int(input("Enter Account No :")))
        self.cname=input("Enter Updated Name :")
        self.city=input("Enter City Name :")
        self.phone=int(input("Enter Phone Number :"))
        cursor.execute("use jaswanth")
        df=pd.read_sql_query("select * from bank",cnxn)
        if ((df['accno']==self.accno)).any():
            cursor.execute("update bank set cname=?,city=?,phonenumber=? where accno=?",self.cname,self.city,self.phone,self.accno)
            cursor.execute("commit")
            print(f'{cursor.rowcount} row affected')
        else:
            print("ACCOUNT DO NOT EXISTS")
            
             


       


b=Bank()
#b.AccountTable()
#b.InsertAccount()
#b.DepositAmount()
#b.WithdrawAmount()
#b.BalanceEnquiry()
#b.PrintAccounts()
#b.CloseAccount()
#b.ModifyAccount()
choice='Y'
while choice=='Y':
    print(" "*18+"*"*27+" "*10)
    print(" "*20+"BANK MANAGEMENT SYSTEM"+" "*10)
    print(" "*18+"*"*27+" "*10+"\n")
    print("MAIN MENU")
    print("1. NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAW AMOUNT")
    print("4. BALANCE ENQUIRY")
    print("5. ALL ACCOUNTS HOLDER LIST")
    print("6. CLOSE AN ACCOUNT")
    print("7. MODIFY AN ACCOUNT")
    print("8. EXIT")
    n=int(input("Select Your Option (1-8) :"))
    if n==1:
        b.InsertAccount()
    elif n==2:
        b.DepositAmount()
    elif n==3:
        b.WithdrawAmount()
    elif n==4:
        b.BalanceEnquiry()
    elif n==5:
        b.PrintAccounts()
    elif n==6:
        b.CloseAccount()
    elif n==7:
        b.ModifyAccount()
    elif n==8:
        sys.exit()
    else:
        print("Invalid input")

cnxn.close()
    
        
        
        
        
        
        
        
        

    

            
    
       
    
        

      



