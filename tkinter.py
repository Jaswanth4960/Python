'''from tkinter  import *
import random
window=Tk()
lbl1=Label(window,text="Create New Account",font = "Helvetica 16 bold")
lbl1.grid(row=0,column=2)
label1=Label(window,text='FirstName ')
label1.grid(row=2,column=1)
en1=Entry(window)
en1.grid(row=2,column=2)
label2=Label(window,text='LastName ')
label2.grid(row=3,column=1)
en2=Entry(window)
en2.grid(row=3,column=2)
label3=Label(window,text="Email-Address ")
label3.grid(row=4,column=1)
en3=Entry(window)
en3.grid(row=4,column=2)
label4=Label(window,text="Password ")
label4.grid(row=5,column=1)
en4=Entry(window)
en4.grid(row=5,column=2)
label5=Label(window,text="Enter OTP ")
label5.grid(row=6,column=1)
en5=Entry(window)
en5.grid(row=6,column=2)
en5.insert(0,random.randint(1000,9999))

namelist=[]
email=[]
pwd=[]
def name():
    fname=en1.get()
    lname=en2.get()
    namee=fname+' '+lname
    namelist.append(namee)
    e=en3.get()
    email.append(e)
    p=en4.get()
    pwd.append(p)
    
    
    
    






btn1=Button(window,text="Verify Result")
btn1.grid(row=6,column=3)
btn2=Button(window,text="Clear")
btn2.grid(row=7,column=1)
btn3=Button(window,text="Register",command=name)
btn3.grid(row=7,column=2)
btn4=Button(window,text="Exit")
btn4.grid(row=7,column=3)

window.mainloop()

print(namelist)
'''


