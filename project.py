from tkinter import *
from item import Items
import mysql.connector
from category import Category
from Warehouse import Warehouse
from products import Products
from orders import Orders
from members import Members



class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Inventory Management System")
        self.root.config(bg="#d3d3d3")
        var1=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",bg='teal',fg='white',font='comicsanms 30 bold',borderwidth=3,relief=SUNKEN)
        var1.pack(fill=X)

        f1 = Frame(self.root, bg = "black",borderwidth=10,relief=SUNKEN)
        f1.pack(side=LEFT,fill=Y)


        b1 = Button(f1, text="Items",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=self.item)
        b1.pack(fill=X)
        b2 = Button(f1, text="Category",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=self.category)
        b2.pack(fill=X)
        b3 = Button(f1, text="Warehouse",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=self.Warehouse)
        b3.pack(fill=X)
    
        b5 = Button(f1, text="Products",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=self.products)
        b5.pack(fill=X)
        b6 = Button(f1, text="Orders",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=self.orders)
        b6.pack(fill=X)
        b7 = Button(f1, text="Members",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=self.members)
        b7.pack(fill=X)
      
        b10 = Button(f1, text="Exit",bg="black",font="Helvetica 10 bold",fg="grey",pady=6, command=quit)
        b10.pack(fill=X)

        self.addItemsLabel = Label(self.root, text="Total items : ", bd=5, relief=SUNKEN, bg="teal", fg="black", font="Helvetica 20 bold")
        self.addItemsLabel.place(x=300, y=120, height=150, width=300)
        
        self.addCategoryLabel = Label(self.root, text="Total Category : ", bd=5, relief=SUNKEN, bg="#cd5c5c", fg="black", font="Helvetica 20 bold")
        self.addCategoryLabel.place(x=650,y=120,height=150,width=300)
        
        self.addWarehouseLabel = Label(self.root, text="Total Warehouse : ", bd=5, relief=SUNKEN, bg="orange", fg="black", font="Helvetica 20 bold")
        self.addWarehouseLabel.place(x=1000,y=120,height=150,width=300)
                
        l4=Label(self.root, text="Total Products : ",bd=5,relief=SUNKEN,bg="lavender", fg="black", font="Helvetica 20 bold")
        
        self.addUnpaidLabel = Label(self.root, text="Unpaid orders : ", bd=5, relief=SUNKEN, bg="olive", fg="black", font="Helvetica 20 bold")
        self.addUnpaidLabel.place(x=650,y=300,height=150,width=300)

        self.addPaidLabel = Label(self.root, text="Paid orders : ", bd=5, relief=SUNKEN, bg="#87cefa", fg="black", font="Helvetica 20 bold")
        self.addPaidLabel.place(x=1000,y=300,height=150,width=300)

        self.addMembersLabel = Label(self.root, text="Total Members : ", bd=5, relief=SUNKEN, bg="grey", fg="black", font="Helvetica 20 bold")
        self.addMembersLabel.place(x=300,y=480,height=150,width=300)

        self.addSalesLabel = Label(self.root, text="Total Sales : ", bd=5, relief=SUNKEN, bg="#9370d8", fg="black", font="Helvetica 20 bold")
        self.addSalesLabel.place(x=650,y=480,height=150,width=300)
         
        l4.place(x=300,y=300,height=150,width=300)
        

        self.update_items_label()
        self.update_members_label()
        self.update_Unpaid_orders_label()
        self.update_Paid_orders_label()
        self.update_Category_label()
        self.update_Warehouse_label()
        self.update_Sales_label()

    def update_items_label(self):
        total_items = self.get_total_items()
        self.addItemsLabel.config(text=f"Total items : {total_items}")

    def update_members_label(self):
        total_members = self.get_total_members()
        self.addMembersLabel.config(text=f"Total Members : {total_members}")

    def update_Unpaid_orders_label(self):
        total_unpaid_orders = self.get_total_unpaid_orders()
        self.addUnpaidLabel.config(text=f"Unpaid Orders : {total_unpaid_orders}")

    def update_Paid_orders_label(self):
        total_paid_orders = self.get_total_paid_orders()
        self.addPaidLabel.config(text=f"Paid Orders : {total_paid_orders}")

    def update_Category_label(self):
        total_category = self.get_total_category()
        self.addCategoryLabel.config(text=f"Total Category : {total_category}")

    def update_Warehouse_label(self):
        total_Warehouse = self.get_total_warehouse()
        self.addWarehouseLabel.config(text=f"Total Warehouse : {total_Warehouse}")

    def update_Sales_label(self):
        total_sales = self.get_total_sales()
        self.addSalesLabel.config(text=f"Total Sales : {total_sales}")


    def get_total_items(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT SUM(quantity) AS total_quantity from add_items where Status='Active'")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0
    
    def get_total_members(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) AS total_members from members")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0
        
    def get_total_unpaid_orders(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) AS total_unpaid_orders from orders where payment='Unpaid' ")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0
    
    def get_total_paid_orders(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) AS total_paid_orders from orders where payment='Paid'")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0
    
    def get_total_category(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) AS total_category from category where status='Active'")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0
    
    def get_total_warehouse(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) AS total_warehouse from warehouse where status='Active'")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0
    
    def get_total_sales(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) AS total_sales from orders")
        res = my_cursor.fetchone()
        conn.close()
        return res[0] if res else 0


    def item(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Items(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Category(self.new_win)

    def Warehouse(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Warehouse(self.new_win)


    def products(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Products(self.new_win)

    def orders(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Orders(self.new_win)

    def members(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Members(self.new_win)


if __name__=="__main__":
    root = Tk()
    obj=IMS(root)
    root.mainloop()