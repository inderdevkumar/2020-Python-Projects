import sqlite3
import pandas as pd

df_synsets = pd.read_excel("synsets.xlsx")
df_phrases = pd.read_excel("phrases.xlsx")

def create_table():
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS synsets(SynsetID INTEGER, Definition TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS phrases(SynsetID INTEGER, phrase TEXT)")
    conn.commit()
    conn.close()

def insert_phrases():
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cols = ",".join([str(i) for i in df_phrases.columns.tolist()])
    print(cols)
    # Insert DataFrame records one by one. 
    for i,row in df_phrases.iterrows():
        sql = "INSERT INTO phrases (" + cols + ") VALUES (" + "?,"*(len(row)-1) + "?)"
        cur.execute(sql, tuple(row)) 
    # the connection is not autocommitted by default, so we must commit to save our # changes 
        conn.commit()
        
def insert_synsets():
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cols = ",".join([str(i) for i in df_synsets.columns.tolist()])
    print(cols)
    # Insert DataFrame records one by one. 
    for i,row in df_synsets.iterrows():
        sql = "INSERT INTO synsets (" + cols + ") VALUES (" + "?,"*(len(row)-1) + "?)"
        cur.execute(sql, tuple(row)) 
    # the connection is not autocommitted by default, so we must commit to save our # changes 
        conn.commit()

def view_meaning(SynsetID):
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT * FROM synsets WHERE SynsetID=?", (SynsetID,))
    rows= cur.fetchall()
    conn.close()
    return rows
    
def view_phrase(phrase):
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT * FROM phrases WHERE phrase=?", (phrase,))
    rows= cur.fetchall()
    conn.close()
    return rows    
    
def phrase_count(phrase):
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT COUNT(SynsetID) FROM phrases WHERE phrase=?", (phrase,))
    rows= cur.fetchall()
    conn.close()
    return rows

def unique_synonyms_count(SynsetID):
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT DISTINCT(phrase) FROM phrases WHERE SynsetID=?", (SynsetID,))
    rows= cur.fetchall()
    conn.close()
    return rows






























def delete():
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("DELETE FROM phrases")  # Comma is needed here after item_var for syntax
    conn.commit()
    conn.close()

#create_table()


def view():
    conn= sqlite3.connect("inderdev.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT * FROM phrases")
    rows= cur.fetchall()
    conn.close()
    return rows


#insert_synsets()
#print(view())
