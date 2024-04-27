from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
from Add_Member import Add_Members 

class Members:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080")
        self.root.title("Members")
        self.root.config(bg="white")
        
        var1=Label(self.root,text="Manage Members",bg='lavender',fg='black',font='comicsanms 16 bold',borderwidth=3,relief=RIDGE, pady=30)
        var1.pack(fill=X)

        b1 = Button(var1, text=" Add Member",bg="white",font="Helvetica 10 bold",fg="grey",pady=1, command=self.Add_Members)
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

        Members_frame = Frame(self.root, bd=3, relief=RIDGE)
        Members_frame.place(x=0, y=200, relwidth=1, height=500)

        scrolly=Scrollbar(Members_frame, orient=VERTICAL)
        self.Members_table=ttk.Treeview(Members_frame, columns=("username", "email", "name","phone"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Members_table.yview)

        
        self.Members_table.heading("username", text="Username")
        self.Members_table.heading("email", text="Email")
        self.Members_table.heading("name", text="Name")
        self.Members_table.heading("phone", text="Phone")
       

        self.Members_table["show"]="headings"

        self.Members_table.column("username", width=150)
        self.Members_table.column("email", width=150)
        self.Members_table.column("name", width=150)
        self.Members_table.column("phone", width=150)
       

        self.Members_table.pack(fill=BOTH, expand=1)

        self.Members_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

        self.btn_delete = Button(self.root, text="Delete", bg="red", font="Helvetica 10 bold", fg="white", pady=1, command=self.delete_item)
        self.btn_delete.place(x=10, y=720, width=50, height=25)

        self.btn_update = Button(self.root, text="Update", bg="green", font="Helvetica 10 bold", fg="white", pady=1, command=self.update_item)
        self.btn_update.place(x=80, y=720, width=50, height=25)


    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="IMS")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Username, Email,Name, Phone FROM members")
            rows = my_cursor.fetchall()
            conn.close()
            self.display_data(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")

    def display_data(self, rows):
        self.Members_table.delete(*self.Members_table.get_children())
        for row in rows:
            self.Members_table.insert("", "end", values=row)

    def get_cursor(self, event):
        cursor_row = self.Members_table.focus()
        if cursor_row:
            self.selected_item = self.Members_table.item(cursor_row)
            print(self.selected_item["values"])

    def delete_item(self):
        if hasattr(self, "selected_item"):
            Username = self.selected_item["values"][0]
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM members WHERE Username = %s", (Username,))
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
            Username = self.selected_item["values"][0]
            new_status = "Updated"  # You need to specify the new status here
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE members SET Email = %s WHERE Username = %s", (new_status, Username))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Item updated successfully")
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error updating item: {str(e)}")
        else:
            messagebox.showerror("Error", "No Member selected")

    def Add_Members(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Add_Members(self.new_win)


if __name__=="__main__":
    root = Tk()
    obj = Members(root)
    root.mainloop()