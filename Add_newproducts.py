from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk

class Add_NewProducts:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x680")
        self.root.title("Manage Products")
        self.root.config(bg="white")
        
        var1=Label(self.root,text="Add New Products",bg='lavender',fg='black',font='comicsanms 16 bold',borderwidth=3,relief=RIDGE, pady=12)
        var1.pack(fill=X)
        
        f1 = Frame(self.root, bg = "black",borderwidth=10,relief=SUNKEN)
        f1.pack(fill=Y)
        
        lbl_name=Label(self.root,text="Product Name ",font=("goudy old style",15),bg="white").place(x=30,y=70)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=30,y=100,width=1000,height=35)
        
        lbl_amount=Label(self.root,text="Price ",font=("goudy old style",15),bg="white").place(x=30,y=150)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=30,y=180,width=200,height=35)
        
        lbl_Qty=Label(self.root,text="Qty ",font=("goudy old style",15),bg="white").place(x=300,y=150)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=300,y=180,width=200,height=35)
        
        lbl_description=Label(self.root,text="Description ",font=("goudy old style",15),bg="white").place(x=30,y=230)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=30,y=260,width=1000,height=80)
        
        lbl_color=Label(self.root,text="Color ",font=("goudy old style",15),bg="white").place(x=30,y=365)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=30,y=395,width=200,height=35)
        
        lbl_size=Label(self.root,text="Size ",font=("goudy old style",15),bg="white").place(x=300,y=365)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=300,y=395,width=200,height=35)
        
        lbl_items=Label(self.root,text="Items ",font=("goudy old style",15),bg="white").place(x=30,y=445)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=30,y=475,width=1000,height=35)
        
        lbl_category=Label(self.root,text="Currency :",font=("goudy old style",15),bg="white").place(x=30,y=525)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="white")
        self.txt_address.place(x=30,y=555,width=1000,height=35)

        f4 = Frame(self.root, bg = "white",borderwidth=0,relief=SUNKEN)
        f4.place(x=0, y=600, height=70, width=456)

        b1 = Button(f4, text="Close",bg="red",font="Helvetica 10 bold",fg="white",pady=1, command=root.destroy)
        b1.place(x=30, y=20, height=25,width=50)

        b2 = Button(f4, text="Save Changes",bg="green",font="helvetica 10 bold",fg="white",pady=1)
        b2.place(x=100, y=20, height=25,width=100)
        
if __name__=="__main__":
    root = Tk()
    obj = Add_NewProducts(root)
    root.mainloop()