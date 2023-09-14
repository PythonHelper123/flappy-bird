from tkinter import *
from tkinter import ttk



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="AHA LIBRARY MANAGEMENT",bg ="Maroon", fg="white",bd =20,relief =RIDGE,font =("times new roman ", 50 ,"bold" ),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE ,padx=20,bg="Maroon")
        frame.place(x=0,y=110,width =1550,height=400)

        #Dataframeleft

        DataFrameLeft=LabelFrame(frame,text="Member Information",bg ="Maroon", fg="white",bd =12,relief =RIDGE,font =("times new roman ", 12 ,"bold" ))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="Maroon",fg="White",text="Member Type",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        coMember=ttk.Combobox(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=27,state="readonly")
        coMember["value"]=["Admin Staff","Student","Lecturer"]
        coMember.grid(row=0,column=1)

        lblPRN=Label(DataFrameLeft,bg="Maroon",fg="White",text="PRN No ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblPRN.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="Maroon",fg="White",text="Title ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="Maroon",fg="White",text="First Name ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="Maroon",fg="White",text="Last Name  ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="Maroon",fg="White",text="Address Pri ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="Maroon",fg="White",text="Address Sec ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="Maroon",fg="White",text="Post Code ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="Maroon",fg="White",text="Mobile",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="Maroon",fg="White",text="Book ID ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="Maroon",fg="White",text="Book Title ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="Maroon",fg="White",text="Author Name  ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="Maroon",fg="White",text="Date Borrowed ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="Maroon",fg="White",text="Date Due ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDateDue.grid(row=4,column=3)

        lblDaysonbook=Label(DataFrameLeft,bg="Maroon",fg="White",text="Days on book",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDaysonbook.grid(row=5,column=2,sticky=W)
        txtDaysonbook=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDaysonbook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="Maroon",fg="White",text="Late Return Fine ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverDue=Label(DataFrameLeft,bg="Maroon",fg="White",text="Date Over Due ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtDateOverDue.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,bg="Maroon",fg="White",text="Actual Price ",font=("times new roman ", 12 ,"bold" ),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman ", 12 ,"bold" ),width=28)
        txtActualPrice.grid(row=8,column=3)

        #Dataframe right

    


        DataFrameRight=LabelFrame(frame,text="Book Details",bg ="Maroon", fg="white",bd =12,relief =RIDGE,font =("times new roman ", 12 ,"bold" ))
        DataFrameRight.place(x=901,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font =("times new roman ", 12 ,"bold" ),width=32, height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['To Kill a Mockingbird', 'Pride and Prejudice', 'The Great Gatsby', '1984', 'The Catcher in the Rye', 'Brave New World', 'The Lord of the Rings', 'The Hobbit', 'Moby-Dick', 'The Grapes of Wrath', 'The Scarlet Letter', 'War and Peace', 'The Odyssey', 'The Alchemist', 'The Hunger Games','Moby-Dick', 'The Grapes of Wrath', 'The Scarlet Letter', 'War and Peace', 'The Odyssey', 'The Alchemist', 'The Hunger Games', 'The Da Vinci Code', 'The Shining', 'Gone with the Wind', 'The Chronicles of Narnia', 'The Road', 'Fahrenheit 451', 'Crime and Punishment', 'Wuthering Heights', 'The Sun Also Rises', 'The Old Man and the Sea', 'One Hundred Years of Solitude', 'To the Lighthouse', 'The Stranger', 'The Bell Jar', 'A Tale of Two Cities']
        listBox=Listbox(DataFrameRight,font =("times new roman ", 12 ,"bold" ),width=20,height=16,yscrollcommand=listScrollbar.set)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        #Buttons Frame

        framebutton=Frame(self.root,bd=12,relief=RIDGE ,padx=20,bg="Maroon")
        framebutton.place(x=0,y=510,width =1550,height=70)

        btnAddData=Button(framebutton,text="Add Data",font =("times new roman ", 12 ,"bold" ),width=23,bg="Maroon",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,text="Show Data",font =("times new roman ", 12 ,"bold" ),width=23,bg="Maroon",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,text="Update ",font =("times new roman ", 12 ,"bold" ),width=23,bg="Maroon",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,text="Delete",font =("times new roman ", 12 ,"bold" ),width=23,bg="Maroon",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(framebutton,text="Reset",font =("times new roman ", 12 ,"bold" ),width=23,bg="Maroon",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,text="Exist",font =("times new roman ", 12 ,"bold" ),width=23,bg="Maroon",fg="white")
        btnAddData.grid(row=0,column=5)

        

        #Information Frame
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE ,padx=20,bg="Maroon")
        FrameDetails.place(x=0,y=580,width =1550,height=220)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="Maroon")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame, column=("membertype", "prnno", "title", "firstname", "lastname", "pri add", "sec add", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member type")
        self.library_table.heading("prnno",text="PRN no")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("pri add",text="Address1")
        self.library_table.heading("sec add",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID ")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of issue")
        self.library_table.heading("datedue",text="Due Date")
        self.library_table.heading("days",text="Days on book ")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverdue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
       
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    
