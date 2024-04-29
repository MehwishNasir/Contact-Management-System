import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Establish connection to MySQL database
connect = mysql.connector.connect(
    host='localhost',
    username='root',
    password='nasirmehwish03',
    database='contact_book'
)
cursor = connect.cursor(buffered=True)
cursor.execute('USE contact_book')
# Ensure table exists
try:
    cursor.execute('DESC contactlist')
except mysql.connector.Error:
    cursor.execute('''CREATE TABLE contactlist(
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(20),
                      phone INT,
                      email VARCHAR(30),
                      address VARCHAR(50)
                      )''')

# Function to add a contact to the database
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Validate input
    if not name or not phone or not email or not address:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Insert contact into the database
    try:
        cursor.execute('''INSERT INTO contactlist(name, phone, email, address) 
                       VALUES (%s, %s, %s, %s)''', (name, phone, email, address))
        messagebox.showinfo("Success", "Contact added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")

# Function to remove a contact from the database
def remove_contact():
    name = name_entry.get()

    # Validate input
    if not name:
        messagebox.showerror("Error", "Please enter a name to remove")
        return

    # Remove contact from the database
    try:
        cursor.execute("DELETE FROM contactlist WHERE name = %s", (name,))
        connect.commit()
        messagebox.showinfo("Success", f"Contact {name} removed successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")

# Create the main window
root = tk.Tk()
root.title("Contacts Management System")

# Set window size and position
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set window background color
root.configure(bg="#FFFFFF")

# Create labels and entry fields with styling
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
entry_width = 30
entry_bg = "#FFFFFF"
entry_fg = "#000000"

tk.Label(root, text="Name:", font=label_font, bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root, width=entry_width, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief=tk.SOLID)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Phone:", font=label_font, bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, sticky="w")
phone_entry = tk.Entry(root, width=entry_width, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief=tk.SOLID)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Email:", font=label_font, bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(root, width=entry_width, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief=tk.SOLID)
email_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Address:", font=label_font, bg="#FFFFFF").grid(row=3, column=0, padx=10, pady=10, sticky="w")
address_entry = tk.Entry(root, width=entry_width, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief=tk.SOLID)
address_entry.grid(row=3, column=1, padx=10, pady=10)

# Create Add Contact button with styling
add_button = tk.Button(root, text="Add Contact", font=label_font, bg="#4CAF50", fg="#FFFFFF", bd=0, relief=tk.FLAT, command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Create Remove Contact button with styling
remove_button = tk.Button(root, text="Remove Contact", font=label_font, bg="#FF5733", fg="#FFFFFF", bd=0, relief=tk.FLAT, command=remove_contact)
remove_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

root.mainloop()
