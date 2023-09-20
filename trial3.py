from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime, timedelta
import tkinter
import json

fh=open("library.txt","r")
a=fh.read()
listBooks=(a.split(","))




# Initialize an empty dictionary to store book details
book_details = {}

# Read the text file line by line
with open("bookinfo.txt", "r") as file:
    for line in file:
        # Split the line into book title and book details using '+'
        parts = line.strip().split('+')
        if len(parts) == 2:
            book_title, details_str = parts
            try:
                # Convert the details string to a dictionary using eval()
                book_details[book_title] = eval(details_str)
            except SyntaxError:
                # Handle any syntax errors in the details string
                print(f"Skipping line with syntax error: {line}")
        else:
            print(f"Skipping line with incorrect format: {line}")

# Now 'book_details' contains the desired dictionary



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # variable
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()

        lbltitle = Label(self.root, text="AHA LIBRARY MANAGEMENT", bg="Maroon", fg="white", bd=20, relief=RIDGE,
                         font=("times new roman ", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="Maroon")
        frame.place(x=0, y=110, width=1550, height=800)

        # Dataframeleft

        DataFrameLeft = LabelFrame(frame, text="Member Information", bg="Maroon", fg="white", bd=12, relief=RIDGE,
                                   font=("times new roman ", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="Maroon", fg="White", text="Member Type",
                          font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        coMember = ttk.Combobox(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.member_var,
                                width=27, state="readonly")
        coMember["value"] = ["Admin Staff", "Student", "Lecturer"]
        coMember.grid(row=0, column=1)

        lblPRN = Label(DataFrameLeft, bg="Maroon", fg="White", text="PRN No ", font=("times new roman ", 12, "bold"),
                       padx=2, pady=6)
        lblPRN.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.prn_var, width=28)
        txtPRN_NO.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg="Maroon", fg="White", text="Title ", font=("times new roman ", 12, "bold"),
                         padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.id_var, width=28)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="Maroon", fg="White", text="First Name ",
                             font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.firstname_var,
                             width=28)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="Maroon", fg="White", text="Last Name  ",
                            font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.lastname_var,
                            width=28)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="Maroon", fg="White", text="Address Pri ",
                            font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.address1_var,
                            width=28)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="Maroon", fg="White", text="Address Sec ",
                            font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.address2_var,
                            width=28)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="Maroon", fg="White", text="Post Code ",
                            font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.postcode_var,
                            width=28)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="Maroon", fg="White", text="Mobile", font=("times new roman ", 12, "bold"),
                          padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.mobile_var, width=28)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, bg="Maroon", fg="White", text="Book ID ",
                          font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.bookid_var, width=28)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="Maroon", fg="White", text="Book Title ",
                             font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.booktitle_var,
                             width=28)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg="Maroon", fg="White", text="Author Name  ",
                          font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.author_var, width=28)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="Maroon", fg="White", text="Date Borrowed ",
                                font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"),
                                textvariable=self.dateborrowed_var, width=28)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="Maroon", fg="White", text="Date Due ",
                           font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.datedue_var,
                           width=28)
        txtDateDue.grid(row=4, column=3)

        lblDaysonbook = Label(DataFrameLeft, bg="Maroon", fg="White", text="Days on book",
                              font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblDaysonbook.grid(row=5, column=2, sticky=W)
        txtDaysonbook = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.daysonbook_var,
                              width=28)
        txtDaysonbook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="Maroon", fg="White", text="Late Return Fine ",
                                  font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"),
                                  textvariable=self.latereturnfine_var, width=28)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="Maroon", fg="White", text="Date Over Due ",
                               font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.dateoverdue,
                               width=28)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="Maroon", fg="White", text="Actual Price ",
                               font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"), textvariable=self.finallprice,
                               width=28)
        txtActualPrice.grid(row=8, column=3)

        # Dataframe right

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="Maroon", fg="white", bd=12, relief=RIDGE,
                                    font=("times new roman ", 12, "bold"))
        DataFrameRight.place(x=901, y=5, width=540, height=350)

        self.txtBox = Text(DataFrameRight, font=("times new roman ", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")


        # Assuming you have a dictionary with book details
        

        # Add more book details as needed

        # ... other book details ...

        def SelectBook(event=""):
            # Get the selected book from the listbox
            selected_book = listBox.get(listBox.curselection())

            # Check if the selected book is in the book_details dictionary
            if selected_book in book_details:
                book = book_details[selected_book]
                # Update the entry fields with book details
                self.bookid_var.set(book["bookid"])
                self.booktitle_var.set(book["booktitle"])
                self.author_var.set(book["author"])

                d1 = datetime.today()
                d2 = timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finallprice.set("Rs.1000")
                # ... update other entry fields as needed ...

            else:
                messagebox.showerror("Error", "Book details not found for the selected book.")

        listBox = Listbox(DataFrameRight, font=("times new roman ", 12, "bold"), width=20, height=16,
                          yscrollcommand=listScrollbar.set)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # Buttons Frame

        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="Maroon")
        framebutton.place(x=0, y=510, width=1550, height=70)

        btnAddData = Button(framebutton, command=self.add_data, text="Add Data", font=("times new roman ", 12, "bold"),
                            width=23, bg="Maroon", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(framebutton,command=self.showData, text="Show Data", font=("times new roman ", 12, "bold"), width=23, bg="Maroon",
                            fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(framebutton,command=self.update ,text="Update ", font=("times new roman ", 12, "bold"), width=23, bg="Maroon",
                            fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(framebutton,command=self.delete, text="Delete", font=("times new roman ", 12, "bold"), width=23, bg="Maroon",
                            fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(framebutton,command=self.reset ,text="Reset", font=("times new roman ", 12, "bold"), width=23, bg="Maroon",
                            fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(framebutton,command=self.iExit, text="Exit", font=("times new roman ", 12, "bold"), width=23, bg="Maroon",
                            fg="white")
        btnAddData.grid(row=0, column=5)

        # Information Frame
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="Maroon")
        FrameDetails.place(x=0, y=580, width=1550, height=220)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="Maroon")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=(
            "membertype", "prnno", "title", "firstname", "lastname", "pri add", "sec add", "postid", "mobile", "bookid",
            "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),
                                          xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member type")
        self.library_table.heading("prnno", text="PRN no")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("pri add", text="Address1")
        self.library_table.heading("sec add", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID ")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date of issue")
        self.library_table.heading("datedue", text="Due Date")
        self.library_table.heading("days", text="Days on book ")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverdue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        # to minimise size

        self.library_table.column("membertype", width=100)



        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="library")
        my_cursor = conn.cursor()

        my_cursor.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),
                           self.prn_var.get(),
                           self.id_var.get(),
                           self.firstname_var.get(),
                           self.lastname_var.get(),
                           self.address1_var.get(),
                           self.address2_var.get(),
                           self.postcode_var.get(),
                           self.mobile_var.get(),
                           self.bookid_var.get(),
                           self.booktitle_var.get(),
                           self.author_var.get(),
                           self.dateborrowed_var.get(),
                           self.datedue_var.get(),
                           self.daysonbook_var.get(),
                           self.latereturnfine_var.get(),
                           self.dateoverdue.get(),
                           self.finallprice.get()
                           ))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success!", "Member has been inserted successfully.")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="library")
        my_cursor = conn.cursor()

        my_cursor.execute("update new_table set member=%s,ID=%s,Firstname=%s,Lastname=%s,Address1=%s,Address2=%s,PostID=%s,Mobile=%s,BookID=%s,BookTitle=%s,Author=%s,Dateborrowed=%s,DateDue=%s,Daysonbook=%s,`latereturnfine`=%s,Dateoverdue=%s,actualprice=%s where PRN_NO=%s",
                                            (self.member_var.get(),
                                             self.id_var.get(),
                                             self.firstname_var.get(),
                                             self.lastname_var.get(),
                                             self.address1_var.get(),
                                             self.address2_var.get(),
                                             self.postcode_var.get(),
                                             self.mobile_var.get(),
                                             self.bookid_var.get(),
                                             self.booktitle_var.get(),
                                             self.author_var.get(),
                                             self.dateborrowed_var.get(),
                                             self.datedue_var.get(),
                                             self.daysonbook_var.get(),
                                             self.latereturnfine_var.get(),
                                             self.dateoverdue.get(),
                                             self.finallprice.get(),
                                             self.prn_var.get()))
                           
            
        conn.commit()
        self.fetch_data()
        self.reset()
        self.showData()
        conn.close()

        messagebox.showinfo("Sucess!","Member has been updated.")
        

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from new_table")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finallprice.set(row[17])
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No\t\t"+ self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID no\t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name\t\t"+ self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name\t\t"+ self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address 1\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address 2\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END,"PostCode\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile no\t\t"+ self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book id\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book title\t\t"+ self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"author\t\t"+ self.author_var.get()+"\n")
        self.txtBox.insert(END,"Dateborrowed\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Due date\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"daysonbook\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"latereturnfine\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"dateovedue\t\t"+ self.dateoverdue.get()+"\n")
        self.txtBox.insert(END,"finall price \t\t"+ self.finallprice.get()+"\n")


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue.set(""),
        self.finallprice.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("error","first select member")

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="library")
            my_cursor = conn.cursor()
            query="delete from new_table where PRN_NO=%s"
            value=(self.prn_var.get())
            
            my_cursor.execute(query, (value,))


            conn.commit()
            self.fetch_data()
            self.reset()
            self.showData()
            conn.close()

            messagebox.showinfo("Sucess","Member has been deleted")




class UpdateWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        

    

        # variable
        self.BookName_var = StringVar()
        self.BookID_var = StringVar()
        self.BookTitle_var= StringVar()
        self.Author_var = StringVar()
        """

        frame = Frame(self.root, bd=12, relief=FLAT, padx=20, bg="Maroon")
        frame.place(x=0, y=110, width=1550, height=400)"""

        lbltitle = Label(self.root, text="AHA LIBRARY MANAGEMENT", bg="Maroon", fg="white", bd=20, relief=RIDGE,
                         font=("times new roman ", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="Maroon")
        frame.place(x=0, y=110, width=1550, height=800)



        DataFrameLeft = LabelFrame(frame, text="Member Information", bg="Maroon", fg="white", bd=12, relief=RIDGE,
                                       font=("times new roman ", 12, "bold"))
        DataFrameLeft.place(x=0, y=120, width=1400, height=200)


        lblPRN = Label(DataFrameLeft, bg="Maroon", fg="White", text="Book Name ",
                           font=("times new roman ", 12, "bold"),
                           padx=2, pady=6)
        lblPRN.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"),textvariable=self.BookName_var, width=28)
        txtPRN_NO.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg="Maroon", fg="White", text="Book ID",
                             font=("times new roman ", 12, "bold"),
                             padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"),textvariable=self.BookID_var,  width=28)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="Maroon", fg="White", text="Book Title ",
                                 font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"),textvariable=self.BookTitle_var, 
                                 width=28)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="Maroon", fg="White", text="Author ",
                                font=("times new roman ", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("times new roman ", 12, "bold"),textvariable=self.Author_var,
                                width=28)
        txtLastName.grid(row=4, column=1)

        btnAddData = Button(DataFrameLeft,command=self.Addbooks, text="Addbooks", font=("times new roman ", 12, "bold"), width=23, bg="Maroon",
                            fg="white")
        btnAddData.grid(row=2, column=3)

        
    
    def Addbooks(self):
        a = self.BookName_var.get()
        b = self.BookID_var.get()
        c = self.BookTitle_var.get()
        d = self.Author_var.get()

        # Format the data for library.txt
        library_entry = f"{a},"

        # Format the data for bookinfo.txt
        bookinfo_entry = f"{a}+{{\"bookid\": \"{b}\",\"booktitle\": \"{c}\",\"author\": \"{d}\"}}"

        # Save data to text files
        with open('library.txt', 'a') as library_file:
            library_file.write(library_entry )

        with open('bookinfo.txt', 'a') as bookinfo_file:
            bookinfo_file.write('\n'+bookinfo_entry )

        messagebox.showinfo("Success", "Book added")

            
        

def main():
    # Create the main window
    main_window = Tk()
    main_window.title("Library Management System Launcher")
    main_window.geometry("1550x750+0+0")

    lbltitle = Label(main_window , text="AHA LIBRARY MANAGEMENT", bg="Maroon", fg="white", bd=20, relief=RIDGE,
                         font=("times new roman ", 50, "bold"), padx=2, pady=6)
    lbltitle.pack(side=TOP, fill=X)

        

    # Set the background color to maroon
    main_window.configure(bg="maroon")

    # Create a button to launch the Library Management System
    launch_button = Button(main_window, text="Issue Books", command=lambda: LibraryManagementSystem(main_window),font=("times new roman ", 15, "bold") ,bg="maroon",fg="white",width=25,height=25)
    launch_button.place(x=387, y=200)

    # Create a button to open the update window for adding books
    add_book_button = Button(main_window, text="Update Books", command=lambda: UpdateWindow(main_window),font=("times new roman ", 15, "bold") ,bg="maroon",fg="white",width=25,height=25)
    add_book_button.place(x=800, y=200)

    main_window.mainloop()

if __name__ == "__main__":
    main()

