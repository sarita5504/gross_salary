from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
import random
import time
import datetime

class Add_category:
    def __init__(self, root):
        self.root=root
        self.root.geometry("456x210")
        self.root.title("Manage Category")
        self.root.config(bg="white")
        
        self.var_status=StringVar()
        self.var_name=StringVar()  # Define self.var_name

        var1=Label(self.root,text="Add Category",bg='white',fg='grey',font='comicsansms 16 bold',borderwidth=1,relief=RIDGE, pady=5)
        var1.pack(fill=X)

        lbl_name=Label(self.root,text="Category Name :",font=("goudy old style",15),bg="white").place(x=10,y=40)
        self.txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style",13),bg="white")
        self.txt_name.place(x=170,y=40)

        lbl_status=Label(self.root,text="Status :",font=("goudy old style",15),bg="white").place(x=10,y=100)
        cmb_status=ttk.Combobox(self.root,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=LEFT,font=("goudy old style",13))
        cmb_status.place(x=170,y=100)

        f4 = Frame(self.root, bg = "white",borderwidth=0,relief=SUNKEN)
        f4.place(x=0, y=150, height=70, width=456)

        b1 = Button(f4, text="Close",bg="red",font="Helvetica 10 bold",fg="white",pady=1, command=root.destroy)
        b1.place(x=260, y=20, height=25,width=50)

        b2 = Button(f4, text="Save Changes",bg="green",font="helvetica 10 bold",fg="white",pady=1,command=self.database_connector)
        b2.place(x=320, y=20, height=25,width=100)
        
    def database_connector(self):
        if self.var_name.get()=="":
             messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="IMS")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO category (category_name, status) VALUES (%s, %s)", (self.var_name.get(), self.var_status.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

if __name__=="__main__":
    root = Tk()
    obj = Add_category(root)
    root.mainloop()