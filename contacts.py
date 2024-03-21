from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

window=Tk()
window.title("Contact List")
width = 700
height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width,height,x, y))
window.resizable(0, 0)
window.config(bg="#6666ff")



FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()

'''def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[4])
    ADDRESS.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()'''
        






Top = Frame(window, width=10)
Top.pack(side=TOP)

Mid = Frame(window, width=500,  bg="#6666ff")
Mid.pack(side=TOP)

MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)

MidLeftPadding = Frame(Mid, width=370, bg="#6666ff")
MidLeftPadding.pack(side=LEFT)

MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)

TableMargin = Frame(window, width=500)
TableMargin.pack(side=TOP)



scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
'''
tree.bind('<Double-Button-1>', OnSelected)'''












def NewWindow():
    newwindow=Tk()
    newwindow.title("Contact List")
    width = 400
    height = 300
    screen_width = newwindow.winfo_screenwidth()
    screen_height = newwindow.winfo_screenheight()
    x = ((screen_width/2) - 400) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    newwindow.resizable(0, 0)
    newwindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    FormTitle = Frame(newwindow)
    FormTitle.pack(side="top")
    ContactForm = Frame(newwindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    RadioGroup.grid(row=3,column=1)
   
 
    label1 = Label(FormTitle, text="Adding New Contacts", font=('arial', 16),bg='#66ff66',fg="black", width=500,borderwidth=1,relief='solid')
    label1.pack(fill=X)
    label2=Label(ContactForm,text="First Name ",font=('arial', 14))
    label2.grid(row=1,column=0)
    entry1=Entry(ContactForm)
    entry1.grid(row=1,column=1)
    label3=Label(ContactForm,text="Last Name ",font=('arial', 14))
    label3.grid(row=2,column=0)
    entry2=Entry(ContactForm)
    entry2.grid(row=2,column=1)
    label4=Label(ContactForm,text="Gender ",font=('arial',14))
    label4.grid(row=3,column=0)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup,text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    label5=Label(ContactForm,text="Age ",font=('arial',14))
    label5.grid(row=4,column=0)
    entry3=Entry(ContactForm)
    entry3.grid(row=4,column=1)
    label5=Label(ContactForm,text="Address ",font=('arial',14))
    label5.grid(row=5,column=0)
    entry4=Entry(ContactForm)
    entry4.grid(row=5,column=1)
    label6=Label(ContactForm,text="Contact ",font=('arial',14))
    label6.grid(row=6,column=0)
    entry5=Entry(ContactForm)
    entry5.grid(row=6,column=1)
    button_save=Button(ContactForm,text="Save ",width=20)
    button_save.grid(row=7,column=1)
    
    
    
  



lbl_title = Label(Top, text="Contact Management System", font=('arial', 16), width=500,borderwidth=1,relief='solid')
lbl_title.pack(fill=X)

button1=Button(MidLeft,width=10,height=1,text="+ ADD NEW",bg='Lawn Green',command=NewWindow).pack(padx=(100,0),side='left',anchor='nw')
button2=Button(MidLeft,width=10,height=1,text="DELETE",bg='Red').pack(padx=(300,0),side='left',anchor='nw')
