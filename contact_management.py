from tkinter import *
import pyodbc
import pandas.io.sql as psql
import tkinter.ttk as ttk
from tkinter import messagebox

##========================================================================
c=Tk()
c.title("Contact Management System")
width = 700
height = 400
screen_width = c.winfo_screenwidth()
screen_height = c.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
c.geometry("%dx%d+%d+%d" % (width, height, x, y))
c.resizable(0, 0)
c.config(bg="#6666FF")

#VARIABLES
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()

##=======================DATABASE CONNECTION==============================
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DESKTOP-UKA5IHV;'
                      'DATABASE=jaswanth;'
                      'Trusted_Connection=Yes;')

cursor = cnxn.cursor()

##=======================TABLE DATA=======================================
def JioDatabase():
    cursor.execute("SELECT * FROM contacts ORDER BY lastname")
    f=cursor.fetchall()
    for data in f:
        #cleaned_data = [str(item).strip("'") for item in data]
        tree.insert('','end',values=(data))

##=======================INSERTING Data/SUBMIT DATA=======================
def SubmitData():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        cursor.execute("INSERT INTO CONTACTS(firstname, lastname, gender, age, address, contact) VALUES (?, ?, ?, ?, ?, ?)", str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()))
        cnxn.commit()
        cursor.execute("SELECT TOP 1 * FROM Contacts ORDER BY per_id DESC")
        new_data = cursor.fetchone()
        cleaned_data = [str(item).strip("'") for item in new_data]
        tree.insert('', 'end', values=cleaned_data)
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")



##=======================SELECT THE DATA==================================

def OnSelected(event):
    global per_id, UpdateWindow
    curItem = tree.focus()
    contents = tree.item(curItem)
    selecteditem = contents['values']
    per_id = selecteditem[0]
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[4])
    ADDRESS.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Update the Contact Management System")
    width = 400
    height = 300
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    UpdateWindow.resizable(0, 0)
    if 'NewWindow' in globals():
        NewWindow.destroy()

    # Frames
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 14)).pack(side=LEFT)
    Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 14)).pack(side=LEFT)

    # Labels
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange", width=300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First name", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last name", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    # Entry
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE, font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS, font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT, font=('arial', 14))
    contact.grid(row=5, column=1)

    # Buttons
    btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)

##========================DELETE THE DATA=========================

def DeleteData():
    if not tree.selection():
        messagebox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = messagebox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = tree.item(curItem)
            selecteditem = contents['values']
            tree.delete(curItem)
            per_id=int(selecteditem[0])
            cursor.execute("DELETE FROM contacts  where per_id = ?", per_id)
            cnxn.commit()

##========================NEW CONTACTS WINDOW======================

def AddNewWindow():
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    NewWindow = Toplevel()
    NewWindow.title("New Contact Window")
    width = 400
    height = 300
    screen_width = c.winfo_screenwidth()
    screen_height = c.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #FRAMES
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    #LABELS
    lbl_title = Label(FormTitle, text="Adding New Contacts", font=('arial', 16), bg="#87ceeb",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First name", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last name", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    #ENTRY
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=5, column=1)
    

    #BUTTONS
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)

#============================FRAMES======================================
Top = Frame(c, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(c, width=500,  bg="#6666FF")
Mid.pack(side=TOP)
MidLeft=Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#6666FF")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(c, width=500)
TableMargin.pack(side=TOP)

#============================LABELS======================================
lbl_title = Label(Top, text="Contact Management System", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+ ADD NEW", bg="Lawn Green", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================

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
tree.bind('<Double-Button-1>', OnSelected)
'''

#============================INITIALIZATION==============================
if __name__=='__main__':
    JioDatabase()
    c.mainloop()
