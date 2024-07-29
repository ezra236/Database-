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

# Function to insert data into the database
def insert_data():
    name = name_entry.get()
    admission_number = admission_entry.get()
    dob = dob_entry.get()
    email = email_entry.get()
    course = course_entry.get()
    
    if name and admission_number and dob and email and course:
        try:
            database = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="StudentPortal"
            )
            cursor = database.cursor()
            sql = "INSERT INTO Students (Name, AdmissionNumber, DateOfBirth, Email, Course) VALUES (%s, %s, %s, %s, %s)"
            values = (name, admission_number, dob, email, course)
            cursor.execute(sql, values)
            database.commit()
            database.close()
            messagebox.showinfo("Success", "Data inserted successfully")
            display_data()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields are required")

# Function to display data in the treeview
def display_data():
    tree.delete(*tree.get_children())
    rows = fetch_data()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Set up the main window
root = tk.Tk()
root.title("Students Data")
root.geometry("800x600")  # Set the window size

# Style configuration
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#ADD8E6", foreground="black")
style.configure("Treeview", font=("Arial", 10), rowheight=25, background="#F0F8FF", fieldbackground="#F0F8FF")

# Set up the form frame
form_frame = tk.Frame(root, bg="#F0F8FF")
form_frame.pack(fill=tk.X, padx=5, pady=5)

tk.Label(form_frame, text="Name:", bg="#F0F8FF").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

tk.Label(form_frame, text="Admission Number:", bg="#F0F8FF").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
admission_entry = tk.Entry(form_frame)
admission_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

tk.Label(form_frame, text="Date of Birth (YYYY-MM-DD):", bg="#F0F8FF").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
dob_entry = tk.Entry(form_frame)
dob_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

tk.Label(form_frame, text="Email:", bg="#F0F8FF").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
email_entry = tk.Entry(form_frame)
email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

tk.Label(form_frame, text="Course:", bg="#F0F8FF").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
course_entry = tk.Entry(form_frame)
course_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

add_button = tk.Button(form_frame, text="Add Student", command=insert_data)
add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

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
