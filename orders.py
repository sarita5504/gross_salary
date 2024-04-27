from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
from Add_neworders import Add_NewOrders

class Orders:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Orders")
        self.root.config(bg="white")
        
        var1=Label(self.root,text="Manage Orders",bg='lavender',fg='black',font='comicsanms 16 bold',borderwidth=3,relief=RIDGE, pady=30)
        var1.pack(fill=X)

        b1 = Button(var1, text="Add Orders",bg="white",font="Helvetica 10 bold",fg="grey",pady=1, command=self.Add_NewOrders)
        b1.place(x=10, y=40, height=40,width=80)

        b2 = Button(var1, text="Close",bg="white",font="helvetica 10 bold",fg="grey",pady=1, command=root.destroy)
        b2.place(x=1430, y=40, height=40,width=80)

        f1 = Frame(self.root, bg = "black",borderwidth=10,relief=SUNKEN)
        f1.pack(fill=Y)

        Orders_frame = Frame(self.root, bd=3, relief=RIDGE)
        Orders_frame.place(x=0, y=200, relwidth=1, height=500)

        scrolly=Scrollbar(Orders_frame, orient=VERTICAL)
        self.Orders_table=ttk.Treeview(Orders_frame, columns=("Bill No", "client", "Contact", "Payment", "Amount"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Orders_table.yview)

        
        self.Orders_table.heading("Bill No", text="Bill No")
        self.Orders_table.heading("client", text="client")
        self.Orders_table.heading("Contact", text="Contact")
        self.Orders_table.heading("Payment", text="Payment")        
        self.Orders_table.heading("Amount", text="Amount")
        

        self.Orders_table["show"]="headings"

        self.Orders_table.column("Bill No", width=150)
        self.Orders_table.column("client", width=150)
        self.Orders_table.column("Contact", width=150)
        self.Orders_table.column("Payment", width=150)
        self.Orders_table.column("Amount", width=150)


        self.Orders_table.pack(fill=BOTH, expand=1)

        self.fetch_data()

        self.btn_delete = Button(self.root, text="Delete", bg="red", font="Helvetica 10 bold", fg="white", pady=1, command=self.delete_item)
        self.btn_delete.place(x=10, y=720, width=50, height=25)

        self.btn_update = Button(self.root, text="Update", bg="green", font="Helvetica 10 bold", fg="white", pady=1, command=self.update_item)
        self.btn_update.place(x=80, y=720, width=50, height=25)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="IMS")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT order_id, client_name, phone, payment, Netamt FROM orders")
            rows = my_cursor.fetchall()
            conn.close()
            self.display_data(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")

    def display_data(self, rows):
        self.Orders_table.delete(*self.Orders_table.get_children())
        for row in rows:
            self.Orders_table.insert("", "end", values=row)

    def get_cursor(self, event):
        cursor_row = self.Orders_table.focus()
        if cursor_row:
            self.selected_item = self.Orders_table.item(cursor_row)
            print(self.selected_item["values"])

    def delete_item(self):
        if hasattr(self, "selected_item"):
            order_id = self.selected_item["values"][0]
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Item deleted successfully")
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting item: {str(e)}")
        else:
            messagebox.showerror("Error", "No item selected")

    def update_item(self):
        if hasattr(self, "selected_item"):
            order_id = self.selected_item["values"][0]
            new_status = "Updated"  
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE orders SET payment = %s WHERE order_id = %s", (new_status, order_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Item updated successfully")
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error updating item: {str(e)}")
        else:
            messagebox.showerror("Error", "No item selected")


    def Add_NewOrders(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Add_NewOrders(self.new_win)




if __name__=="__main__":
    root = Tk()
    obj = Orders(root)
    root.mainloop()