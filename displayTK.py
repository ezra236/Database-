import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk

# Function to fetch data from the database
def fetch_data():
    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="StudentPortal"
        )
        cursor = database.cursor()
        cursor.execute("SELECT * FROM Students")
        rows = cursor.fetchall()
        database.close()
        return rows
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []

# Function to display data in the treeview
def display_data():
    rows = fetch_data()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Set up the main window
root = tk.Tk()
root.title("Students Data")
root.geometry("800x400")  # Set the window size

# Style configuration
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#ADD8E6", foreground="black")
style.configure("Treeview", font=("Arial", 10), rowheight=25, background="#F0F8FF", fieldbackground="#F0F8FF")

# Set up the Treeview with scrollbars
tree_frame = tk.Frame(root, bg="#F0F8FF")
tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

scroll_x = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
scroll_y = tk.Scrollbar(tree_frame, orient=tk.VERTICAL)

tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "AdmissionNumber", "DateOfBirth", "Email", "Course"),
                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

tree.heading("ID", text="Student ID")
tree.heading("Name", text="Name")
tree.heading("AdmissionNumber", text="Admission Number")
tree.heading("DateOfBirth", text="Date of Birth")
tree.heading("Email", text="Email")
tree.heading("Course", text="Course")

tree.column("ID", width=80, anchor="center")
tree.column("Name", width=150, anchor="w")
tree.column("AdmissionNumber", width=120, anchor="center")
tree.column("DateOfBirth", width=120, anchor="center")
tree.column("Email", width=200, anchor="w")
tree.column("Course", width=150, anchor="w")

tree.pack(fill=tk.BOTH, expand=True)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_x.config(command=tree.xview)
scroll_y.config(command=tree.yview)

# Fetch and display data
display_data()

# Start the Tkinter main loop
root.mainloop()
