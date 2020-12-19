import mysql.connector

class Database:

    #Connect to Database
    def __init__(self, db): # To inilailse
        self.conn= mysql.connector.connect(
        user="username", # username of your database
        password = "password", #password of your database
        host="108.167.140.122",  #Host ip 
        database = "database")  #Database used
        
        self.cur= self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS test (Movie_Name text, Release_Year integer, Director text, Movie_Type text)")
        self.conn.commit()

    #Adds frecord to Database, Done for Static adding
    def insert(self):
        self.conn= mysql.connector.connect(
        user="username", # username of your database
        password = "password", #password of your database
        host="108.167.140.122",  #Host ip 
        database = "database")  #Database used
        
        self.cur= self.conn.cursor()
        self.cur.execute("INSERT INTO test(Movie_Name, Release_Year, Director, Movie_Type) VALUES ('Gangs of Wasseypur', 2012 , 'Anurag Kashyap', 'Drama')"
        self.conn.commit()

    #Display all data  
    def view(self):
        self.conn= mysql.connector.connect(
        user="username", # username of your database
        password = "password", #password of your database
        host="108.167.140.122",  #Host ip 
        database = "database")  #Database used
        
        self.cur= self.conn.cursor()
        self.cur.execute("SELECT * FROM test")
        rows=self.cur.fetchall()        
        return rows

Database()
