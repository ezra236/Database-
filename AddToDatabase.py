import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
import re

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
    tree.delete(*tree.get_children())  # Clear existing data
    rows = fetch_data()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Function to validate form fields
def validate_fields():
    # Check if all fields are filled out
    if (not name_entry.get() or 
        not admission_number_entry.get() or 
        not dob_entry.get() or 
        not email_entry.get() or 
        not course_entry.get()):
        messagebox.showwarning("Warning", "All fields must be filled out.")
        return False

    # Check if the email is valid
    email = email_entry.get()
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        messagebox.showwarning("Warning", "Invalid email format.")
        return False

    # Check if the date of birth is in the correct format
    dob = dob_entry.get()
    date_regex = r'^\d{4}-\d{2}-\d{2}$'  # Format: YYYY-MM-DD
    if not re.match(date_regex, dob):
        messagebox.showwarning("Warning", "Date of Birth must be in the format YYYY-MM-DD.")
        return False

    return True

# Function to add a new student to the database
def add_student():
    if not validate_fields():
        return  # Exit if validation fails

    name = name_entry.get()
    admission_number = admission_number_entry.get()
    date_of_birth = dob_entry.get()
    email = email_entry.get()
    course = course_entry.get()

    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="StudentPortal"
        )
        cursor = database.cursor()
        cursor.execute("INSERT INTO Students (Name, AdmissionNumber, DateOfBirth, Email, Course) VALUES (%s, %s, %s, %s, %s)",
                       (name, admission_number, date_of_birth, email, course))
        database.commit()
        database.close()
        messagebox.showinfo("Success", "Student added successfully!")
        add_data_window.destroy()  # Close the add data window
        root.deiconify()  # Show the main window
        display_data()  # Refresh the data in the main window
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to create the add data window
def add_data_window():
    global add_data_window
    add_data_window = tk.Toplevel()
    add_data_window.title("Add New Student")
    add_data_window.geometry("400x300")

    tk.Label(add_data_window, text="Name").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_data_window, text="Admission Number").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_data_window, text="Date of Birth").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_data_window, text="Email").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_data_window, text="Course").grid(row=4, column=0, padx=10, pady=5)

    global name_entry, admission_number_entry, dob_entry, email_entry, course_entry
    name_entry = tk.Entry(add_data_window)
    admission_number_entry = tk.Entry(add_data_window)
    dob_entry = tk.Entry(add_data_window)
    email_entry = tk.Entry(add_data_window)
    course_entry = tk.Entry(add_data_window)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    admission_number_entry.grid(row=1, column=1, padx=10, pady=5)
    dob_entry.grid(row=2, column=1, padx=10, pady=5)
    email_entry.grid(row=3, column=1, padx=10, pady=5)
    course_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(add_data_window, text="Add Student", command=add_student).grid(row=5, column=0, columnspan=2, pady=10)
    tk.Button(add_data_window, text="Cancel", command=add_data_window.destroy).grid(row=6, column=0, columnspan=2, pady=10)

# Function to switch to the add data window
def switch_to_add_data():
    root.withdraw()  # Hide the main window
    add_data_window()  # Show the add data window

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

# Add a button to switch to the add data interface
add_button = tk.Button(root, text="Add New Student", command=switch_to_add_data)
add_button.pack(pady=10)

# Fetch and display data
display_data()

# Start the Tkinter main loop
root.mainloop()
