import sqlite3

conn=sqlite3.connect(r'C:\Users\dell\Desktop\dbeaver\weed')


cursor=conn.cursor()


cursor.execute('SELECT * FROM weeds')

results=cursor.fetchall()



for row in results:
    print(row)



cursor.close()
conn.close()
