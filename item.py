from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
from add_item import Add_Item

class Items:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Items Management")
        self.root.config(bg="white")
        
        var1 = Label(self.root, text="Manage Items", bg='lavender', fg='black', font='comicsansms 16 bold', borderwidth=3, relief=RIDGE, pady=30)
        var1.pack(fill=X)

        b1 = Button(var1, text="Add Item", bg="white", font="Helvetica 10 bold", fg="grey", pady=1, command=self.add_item)
        b1.place(x=10, y=40, height=40, width=80)

        b2 = Button(var1, text="Close", bg="white", font="helvetica 10 bold", fg="grey", pady=1, command=root.destroy)
        b2.place(x=1430, y=40, height=40, width=80)

        items_frame = Frame(self.root, bd=3, relief=RIDGE)
        items_frame.place(x=10, y=140, width=1500, height=550)

        self.Items_table = ttk.Treeview(items_frame, columns=("items","quantity", "status"), show="headings")
        self.Items_table.heading("items", text="Items")
        self.Items_table.heading("status", text="Status")
        self.Items_table.heading("quantity", text="Quantity")
        self.Items_table.pack(fill=BOTH, expand=True)

        scroll_y = ttk.Scrollbar(items_frame, orient=VERTICAL, command=self.Items_table.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Items_table.configure(yscrollcommand=scroll_y.set)

        self.Items_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

        # Buttons for delete and update
        self.btn_delete = Button(self.root, text="Delete", bg="red", font="Helvetica 10 bold", fg="white", pady=1, command=self.delete_item)
        self.btn_delete.place(x=10, y=720, width=50, height=25)

        self.btn_update = Button(self.root, text="Update", bg="green", font="Helvetica 10 bold", fg="white", pady=1, command=self.update_item)
        self.btn_update.place(x=80, y=720, width=50, height=25)

    def add_item(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Add_Item(self.new_win)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="IMS")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT item_name, quantity, status FROM add_items")
            rows = my_cursor.fetchall()
            conn.close()
            self.display_data(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}")

    def display_data(self, rows):
        self.Items_table.delete(*self.Items_table.get_children())
        for row in rows:
            self.Items_table.insert("", "end", values=row)

    def get_cursor(self, event):
        cursor_row = self.Items_table.focus()
        if cursor_row:
            self.selected_item = self.Items_table.item(cursor_row)
            print(self.selected_item["values"])

    def delete_item(self):
        if hasattr(self, "selected_item"):
            item_name = self.selected_item["values"][0]
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM add_items WHERE item_name = %s", (item_name,))
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
            item_name = self.selected_item["values"][0]
            new_status = "New Status"  # You need to specify the new status here
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansi#22#06", database="ims")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE add_items SET status = %s WHERE item_name = %s", (new_status, item_name))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Item updated successfully")
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error updating item: {str(e)}")
        else:
            messagebox.showerror("Error", "No item selected")


if __name__ == "__main__":
    root = Tk()
    obj = Items(root)
    root.mainloop()
