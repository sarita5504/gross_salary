from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox

class Add_NewOrders:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900")
        self.root.title("Manage Orders")
        self.root.config(bg="white")

        self.var_name = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()  # Changed to StringVar since phone number may contain characters
        self.var_product = StringVar()
        self.var_quantity = IntVar()
        self.var_rate = IntVar()
        self.var_payment = StringVar()
        self.var_discount = IntVar()
        self.var_Netamt = IntVar()
        
        var1 = Label(self.root, text="Add New Orders", bg='lavender', fg='black', font='comicsansms 16 bold', borderwidth=3, relief=RIDGE, pady=12)
        var1.pack(fill=X)
        
        f1 = Frame(self.root, bg="black", borderwidth=10, relief=SUNKEN)
        f1.pack(fill=Y)
        
        lbl_name = Label(self.root, text="Client Name ", font=("goudy old style", 15), bg="white").place(x=30, y=80)
        self.txt_name = Text(self.root, font=("goudy old style", 15), bg="white")
        self.txt_name.place(x=30, y=110, width=1400, height=35)
        
        lbl_address = Label(self.root, text="Client Address ", font=("goudy old style", 15), bg="white").place(x=30, y=160)
        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="white")
        self.txt_address.place(x=30, y=190, width=1400, height=35)
        
        lbl_phone = Label(self.root, text="Client Phone ", font=("goudy old style", 15), bg="white").place(x=30, y=240)
        self.txt_phone = Text(self.root, font=("goudy old style", 15), bg="white")
        self.txt_phone.place(x=30, y=270, width=1400, height=35)
        
        lbl_product = Label(self.root, text="Product ", font=("goudy old style", 15), bg="white").place(x=30, y=330)
        self.txt_product = Text(self.root, font=("goudy old style", 15), bg="white")
        self.txt_product.place(x=30, y=360, width=300, height=35)
        
        lbl_quantity = Label(self.root, text="Quantity ", font=("goudy old style", 15), bg="white").place(x=400, y=330)
        self.txt_quantity = Entry(self.root, textvariable=self.var_quantity, font=("goudy old style", 15))
        self.txt_quantity.place(x=400, y=360, width=200, height=35)
        
        lbl_rate = Label(self.root, text="Rate ", font=("goudy old style", 15), bg="white").place(x=650, y=330)
        self.txt_rate = Entry(self.root, textvariable=self.var_rate, font=("goudy old style", 15))
        self.txt_rate.place(x=650, y=360, width=100, height=35)

        lbl_payment = Label(self.root, text="Payment :", font=("goudy old style", 15), bg="white").place(x=800, y=330)
        cmb_payment = ttk.Combobox(self.root, textvariable=self.var_payment, values=("Paid", "Unpaid"), state="readonly", justify=LEFT, font=("goudy old style", 15))
        cmb_payment.place(x=800, y=360, height=35, width=400)
        cmb_payment.current(0)

        lbl_discount = Label(self.root, text="Discount ", font=("goudy old style", 12), bg="white").place(x=130, y=440)
        self.txt_discount = Entry(self.root, textvariable=self.var_discount, font=("goudy old style", 12))
        self.txt_discount.place(x=250, y=440, width=300, height=30)
        
        f4 = Frame(self.root, bg="white", borderwidth=0, relief=SUNKEN)
        f4.place(x=0, y=490, height=100, width=1900)

        b1 = Button(f4, text="Create Order", bg="green", font="Helvetica 10 bold", fg="white", pady=1, command=self.database_connector)
        b1.place(x=30, y=30, height=25, width=100)

        b2 = Button(f4, text="Back", bg="red", font="helvetica 10 bold", fg="white", pady=1, command=root.destroy)
        b2.place(x=150, y=30, height=25, width=50)

    def database_connector(self):
        if self.txt_name.get("1.0", END).strip() == "":
             messagebox.showerror("Error", "Client Name is required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO orders (client_name, address, phone, Product, quantity, Rate, payment, Discount, Netamt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  (self.txt_name.get("1.0", END).strip(), 
                   self.txt_address.get("1.0", END).strip(), 
                   self.txt_phone.get("1.0", END).strip(), 
                   self.txt_product.get("1.0", END).strip(), 
                   self.var_quantity.get(), 
                   self.var_rate.get(), 
                   self.var_payment.get(), 
                   self.var_discount.get(), 
                   ((1 - self.var_discount.get() / 100) * self.var_rate.get() * self.var_quantity.get())))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")
        
if __name__ == "__main__":
    root = Tk()
    obj = Add_NewOrders(root)
    root.mainloop()
