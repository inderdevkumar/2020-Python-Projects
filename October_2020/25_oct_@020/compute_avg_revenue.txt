import sqlite3

book_ordered= int(input("Enter the number of book ordered: "))
online_offline= int(input("Enter 1 for online and 0 for offline: "))

#If online
cost= 0
def compute_shiipping_cost():
    if (book_ordered <= 10):
        cost= ((book_ordered*15) + (0.25 * book_ordered))
    else:
        cost= ((book_ordered*15) + 5 )
        
    return cost

              
#If offline
def compute_tax():
    cost= ((book_ordered*15) + (0.08 * 15 * book_ordered))
    return cost


def submit():        
    if (online_offline == 1):
        base_cost= 15*book_ordered
        conn= sqlite3.connect("lite.db")  # This to connect with liite database
        cur= conn.cursor()
        cur.execute("INSERT INTO order_history VALUES(?,?,?)",(book_ordered, online_offline, base_cost))
        conn.commit()
        conn.close()
        print(f"Online shiipping cost for {book_ordered} books: ",compute_shiipping_cost())

    else:
        base_cost= 15*book_ordered
        conn= sqlite3.connect("lite.db")  # This to connect with liite database
        cur= conn.cursor()
        cur.execute("INSERT INTO order_history VALUES(?,?,?)",(book_ordered, online_offline, base_cost))
        conn.commit()
        conn.close()
        print(f"Offline tax for {book_ordered} books: ",compute_tax())

def summary_function():
    conn= sqlite3.connect("lite.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT COUNT(online_offline) FROM order_history where online_offline=1")
    online_count= cur.fetchall()
    
    cur.execute("SELECT COUNT(online_offline) FROM order_history where online_offline=0")
    offline_count= cur.fetchall()

    cur.execute("SELECT SUM(cost) FROM order_history")
    avg_revenue= cur.fetchall()
    
    conn.close()
    print("Number of online orders: ", online_count[0][0])
    print("Number of offline orders: ", offline_count[0][0])
    print("Average revenue across all orders: ", avg_revenue[0][0])
    

def create_table():
    conn= sqlite3.connect("lite.db")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS order_history(book_ordered INTEGER, online_offline INTEGER, cost INTEGER)")
    conn.commit()
    conn.close()


    
if __name__ == "__main__":
    submit()
    summary_function()
