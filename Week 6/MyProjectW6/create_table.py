import sqlite3

# Connect to the existing database or create it
connection = sqlite3.connect("db1")
cursor = connection.cursor()

# Create the login_details table
cursor.execute('''
CREATE TABLE IF NOT EXISTS login_details (
    User_Login TEXT,
    User_password TEXT
)
''')

print("Table 'login_details' created successfully.")

connection.commit()
connection.close()
