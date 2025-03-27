from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3

# Function to validate login
# def validateLogin(username, password):
#     # Connect to the database
#     connection_obj = sqlite3.connect("SalesDB.db")
#     cursor_obj = connection_obj.cursor() # uncomment later if needed 

cursor_obj.execute("SELECT User_password FROM login_details WHERE User_Login=?", (value_username,))
output1 = cursor_obj.fetchone()

if output1 and bcrypt.checkpw(value_password.encode('utf-8'), output1[0]):
    print("Login successful")
    messagebox.showinfo("showinfo", "Correct login and password")
else:
    print("Login failed")
    messagebox.showwarning("Warning", "Incorrect login or password")


    # Retrieve user input
    value_username = username.get()
    value_password = str(password.get())

    # Query to check if the user exists with the provided username and password
    cursor_obj.execute("SELECT * FROM login_details WHERE User_Login=? AND User_password=?", (value_username, value_password))
    output1 = cursor_obj.fetchall()

    # Check if the login details are correct
    if len(output1) > 0:
        print("Login successful")
        messagebox.showinfo("showinfo", "Correct login and password")
    else:
        print("Login failed")
        messagebox.showwarning("Warning", "Incorrect login or password")
    
    # Commit changes and close the connection
    connection_obj.commit()
    connection_obj.close()
5
# Function to register a new customer
# def register_customer(username, password):
#     # Connect to the database
#     connection_obj = sqlite3.connect("SalesDB.db")
#     cursor_obj = connection_obj.cursor()

#     # Create the table if it doesn't exist
#     cursor_obj.execute('''
#     CREATE TABLE IF NOT EXISTS login_details (
#         User_Login TEXT PRIMARY KEY,
#         User_password TEXT
#     )''') # Closing the SQL statement properly

import bcrypt

value_password = str(password.get())

# Hash the password before storing it in the database
hashed_password = bcrypt.hashpw(value_password.encode('utf-8'), bcrypt.gensalt())

cursor_obj.execute("INSERT INTO login_details VALUES(?, ?)", (value_username, hashed_password))

    # Retrieve user input
    value_username = username.get()
    value_password = str(password.get())

    # Ensure the username and password meet length requirements
    if len(value_password) > 5 and len(value_username) > 5:
        # Insert the new user into the database
        cursor_obj.execute("INSERT INTO login_details VALUES(?, ?)", (value_username, value_password))
        messagebox.showinfo("showinfo", "User registered")
    else:
        messagebox.showwarning("Warning", "Username and password must be at least 6 characters long")
    
    # Commit changes and close the connection
    connection_obj.commit()
    connection_obj.close()

# Create main window
tkWindow = Tk()  
tkWindow.geometry('400x250')  
tkWindow.title('Tkinter SQLite Login Form Example')

# Username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# Password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

# Login button
validateLogin_partial = partial(validateLogin, username, password)
loginButton1 = Button(tkWindow, text="Login", command=validateLogin_partial).grid(row=3, column=0)

# Register button
register_customer_partial = partial(register_customer, username, password)
loginButton2 = Button(tkWindow, text="Register", command=register_customer_partial).grid(row=3, column=1)

# Start the GUI event loop
tkWindow.mainloop()