import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to the SQLite database file
conn = sqlite3.connect(r'C:\Users\dell\Desktop\dbeaver\intel')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS weeds (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Type TEXT,
    Quantity INTEGER
)
'''

cursor.execute(create_table_query)

# Commit the changes
conn.commit()

# Show a popup message indicating the table was created successfully
messagebox.showinfo("Table Created", "The 'weeds' table was created successfully.")

# Insert data into the table
data_to_insert = [
    ('Weed1', 'Indica', 10),
    ('Weed2', 'Sativa', 5),
    ('Weed3', 'Hybrid', 15)
]

insert_query = '''
INSERT INTO weeds (Name, Type, Quantity)
VALUES (?, ?, ?)
'''

cursor.executemany(insert_query, data_to_insert)

# Commit the changes
conn.commit()

# Close the cursor to release the resources
cursor.close()

# Close the connection to the database
conn.close()

# Show a popup message indicating data inserted successfully
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Data Inserted", "Data inserted successfully into the 'weeds' table.")
