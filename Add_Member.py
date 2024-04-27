from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox

class Add_Members:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x480")
        self.root.title("Add Members")
        self.root.config(bg="white")
        
        self.var_gender = StringVar()
        self.var_name = StringVar()
        self.var_username = StringVar()
        self.var_phone = IntVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        
        var1 = Label(self.root, text="Add New Members", bg='lavender', fg='black', font='comicsanms 16 bold', borderwidth=3, relief=RIDGE, pady=12)
        var1.pack(fill=X)

        f1 = Frame(self.root, bg="black", borderwidth=10, relief=SUNKEN)
        f1.pack(fill=Y)
        
        lbl_name = Label(self.root, text="Name :", font=("goudy old style", 15), bg="white").place(x=500, y=100)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15))
        self.txt_name.place(x=500, y=130, width=400)
        
        lbl_username = Label(self.root, text="Username :", font=("goudy old style", 15), bg="white").place(x=30, y=100)
        self.txt_username = Entry(self.root, textvariable=self.var_username, font=("goudy old style", 15))
        self.txt_username.place(x=30, y=130, width=400)
        
        lbl_password = Label(self.root, text="Password :", font=("goudy old style", 15), bg="white").place(x=30, y=200)
        self.txt_password = Entry(self.root, textvariable=self.var_password, font=("goudy old style", 15))
        self.txt_password.place(x=30, y=230, width=400)
        
        lbl_email = Label(self.root, text="Email :", font=("goudy old style", 15), bg="white").place(x=500, y=200)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15))
        self.txt_email.place(x=500, y=230, width=400)
        
        lbl_phone = Label(self.root, text="Phone :", font=("goudy old style", 15), bg="white").place(x=500, y=300)
        self.txt_phone = Entry(self.root, textvariable=self.var_phone, font=("goudy old style", 15))
        self.txt_phone.place(x=500, y=330, width=400)
        
        lbl_gender = Label(self.root, text="Gender :", font=("goudy old style", 15), bg="white").place(x=30, y=300)
        
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Female", "Male", "Other"), state="readonly", justify=LEFT, font=("goudy old style", 15))
        cmb_gender.place(x=30, y=330, height=40, width=400)
        cmb_gender.current(0)

        btn_save = Button(self.root, text="Save", font=("goudy old style", 15), bg="green", fg="white", cursor="hand2", command=self.database_connector)
        btn_save.place(x=30, y=400, width=80, height=28)
        
        btn_back = Button(self.root, text="Back", font=("goudy old style", 15), bg="red", fg="white", cursor="hand2", command=root.destroy)
        btn_back.place(x=140, y=400, width=80, height=28)

    def database_connector(self):
        if self.var_name.get() == "" or self.var_username.get() == "" or self.var_password.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO members (Username, Password, Gender, Name, Email, Phone) VALUES (%s, %s, %s, %s, %s, %s)", (self.var_username.get(), self.var_password.get(), self.var_gender.get(), self.var_name.get(), self.var_email.get(), self.var_phone.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

if __name__ == "__main__":
    root = Tk()
    obj = Add_Members(root)
    root.mainloop()
