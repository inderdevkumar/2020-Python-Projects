import sqlite3


#To create table
def create_table():
    conn= sqlite3.connect("lite.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS names(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    conn.commit()
    conn.close()

#To create Insert
def insert(name):
    
    conn= sqlite3.connect("lite.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("INSERT INTO names (name) VALUES(?)",(name,))
    conn.commit()
    conn.close()
    
#To view the database records
def view():
    conn= sqlite3.connect("lite.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT name FROM names")
    rows= cur.fetchall()
    conn.close()
    return rows


#create_table()
