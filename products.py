from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk
from Add_newproducts import Add_NewProducts

class Products:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Manage Product")
        self.root.config(bg="white")
        
        var1=Label(self.root,text="Manage Product",bg='lavender',fg='black',font='comicsanms 16 bold',borderwidth=3,relief=RIDGE, pady=30)
        var1.pack(fill=X)

        b1 = Button(var1, text=" Add Product",bg="white",font="Helvetica 10 bold",fg="grey",pady=1, command=self.Add_NewProducts)
        b1.place(x=10, y=40, height=40,width=100)

        b2 = Button(var1, text="Close",bg="white",font="helvetica 10 bold",fg="grey",pady=1, command=root.destroy)
        b2.place(x=1430, y=40, height=40,width=80)

        f1 = Frame(self.root, bg = "black",borderwidth=10,relief=SUNKEN)
        f1.pack(fill=Y)

        
        a=Label(self.root, text="Search", font = "helvetica 8 bold")
        a.place(x=1200, y=100, height=25,width=60)

        searchval = StringVar()
        searchentry = Entry(self.root, textvariable=searchval, bg="lightyellow", relief=RIDGE)
        searchentry.place(x=1270, y=100, height=25,width=150)

        Product_frame = Frame(self.root, bd=3, relief=RIDGE)
        Product_frame.place(x=0, y=200, relwidth=1, height=500)

        scrolly=Scrollbar(Product_frame, orient=VERTICAL)
        self.Product_table=ttk.Treeview(Product_frame, columns=("Image", "Product", "Price", "Qty", "Warehouse", "Availabilty", "Action"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Product_table.yview)

        
        self.Product_table.heading("Image", text="Image")
        self.Product_table.heading("Product", text="Product")
        self.Product_table.heading("Price", text="Price")
        self.Product_table.heading("Qty", text="Qty")
        self.Product_table.heading("Warehouse", text="Warehouse")
        self.Product_table.heading("Availabilty", text="Availabity")
        self.Product_table.heading("Action", text="Action")

        self.Product_table["show"]="headings"

        self.Product_table.column("Image", width=150)
        self.Product_table.column("Product", width=150)
        self.Product_table.column("Price", width=150)
        self.Product_table.column("Qty", width=150)
        self.Product_table.column("Warehouse", width=150)
        self.Product_table.column("Availabilty", width=150)
        self.Product_table.column("Action", width=150)

        self.Product_table.pack(fill=BOTH, expand=1)

    def Add_NewProducts(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Add_NewProducts(self.new_win)


if __name__=="__main__":
    root = Tk()
    obj = Products(root)
    root.mainloop()