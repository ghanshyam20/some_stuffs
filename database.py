import sqlite3
import tkinter as tk
from tkinter import messagebox
conn=sqlite3.connect(r'C:\Users\dell\Desktop\dbeaver\lolipop')


cursor=conn.cursor()


#create a table
create_table_query='''
CREATE TABLE IF NOT EXISTS weeds(
ID INTEGER PRIMARY KEY,
Name TEXT,
Type TEXT,Quantity INTEGER
)
'''

cursor.execute(create_table_query)

data_to_insert=[
    ('Weed1','Indica',10),
    ('Weed2','Sativa',5),
    ('Weed3','Hybrid',15)
]


insert_query='''
INSERT INTO weeds(Name,Type,Quantity)
VALUES (?,?,?)

'''
cursor.executemany(insert_query,data_to_insert)

conn.commit()

cursor.execute('SELECT *FROM weeds')
results=cursor.fetchall()

for row in results:
    print(row)


cursor.close()
conn.close()

root=tk.Tk()
root.withdraw()
messagebox.showinfo("table created successfullu")
