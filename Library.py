from tkinter import *
from tkinter import ttk



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="AHA LIBRARY MANAGEMENT",bg ="Maroon", fg="white",bd =20,relief =GROOVE,font =("times new roman ", 50 ,"bold" ),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=FLAT ,padx=20,bg="Maroon")
        frame.place(x=0,y=130,width =1550,height=400)

        DataFrameLeft=LabelFrame(frame,text="Membership information",bg ="Maroon", fg="white",bd =10,relief =FLAT,font =("times new roman ", 20 ,"bold" ))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="maroon",text="Member Type",font=("times new roman ", 20 ,"bold" ),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember= ttk.Combobox(DataFrameLeft,font=("times new roman ", 20 ,"bold" ),width=27,state="readonly")
        comMember["value"]=("Admin staff","student","Lecturer")
        comMember.grid(row=0,column=1)

        lbl.PRN_No=Label(DataFrameLeft,bg="maroon",text="PRN No",font=("times new roman ", 20 ,"bold" ),padx=2,pady=6)
        lbl.PRN_No.grid(row=1,column=0,sticky=W)

        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman ", 20 ,"bold" ),padz=2,pady=6)
        txtPRN_NO.grid(row=1,column=0,sticky=W)
        

        DataFrameRight=LabelFrame(frame,text="Book Details ",bg ="Maroon", fg="white",bd =10,relief =FLAT,font =("times new roman ", 20 ,"bold" ))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        #buttons
        Framebutton=Frame(self.root,bd=12,relief=FLAT ,padx=20,bg="Maroon")
        Framebutton.place(x=0,y=530,width =1550,height=70)

        #information
        Framebutton=Frame(self.root,bd=12,relief=FLAT ,padx=20,bg="Maroon")
        Framebutton.place(x=0,y=600,width =1550,height=195)
        
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
