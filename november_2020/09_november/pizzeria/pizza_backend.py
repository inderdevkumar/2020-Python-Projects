import psycopg2

#To Create table in database
def create_table():
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pizza_itemss(pizza_ordered_date TEXT, pizza_types TEXT, Topping_A_price REAL, Topping_B_price REAL, Topping_C_price REAL, pizza_price REAL)")
    conn.commit()
    conn.close()
    
#To insert the data into db
def insert(pizza_ordered_date, pizza_types, Topping_A_price, Topping_B_price, Topping_C_price, pizza_price):
    
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ") # This to connect with liite database
    cur= conn.cursor()
    cur.execute("INSERT INTO pizza_itemss VALUES(%s, %s,%s,%s,%s,%s)", (pizza_ordered_date, pizza_types, Topping_A_price, Topping_B_price, Topping_C_price, pizza_price))
    conn.commit()
    conn.close()


#How many pizzas in total were sold for that day
def pizzas_in_total_for_that_day(pizza_ordered_date):
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT COUNT(pizza_types) FROM pizza_itemss WHERE pizza_ordered_date = %s", (pizza_ordered_date,))
    rows= cur.fetchall()
    conn.close()
    return rows

#How many pizzas in total were sold for that day per pizza type (see below)
def pizzas_in_total_for_that_day_per_pizza_type(pizza_ordered_date):
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT pizza_types, COUNT(pizza_types) FROM pizza_itemss WHERE pizza_ordered_date = %s GROUP BY pizza_types", (pizza_ordered_date,))
    rows= cur.fetchall()
    conn.close()
    return rows

#How much they spent in total
def spent_in_total(pizza_ordered_date):
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT SUM(Topping_A_price), SUM(Topping_B_price), SUM(Topping_C_price) FROM pizza_itemss WHERE pizza_ordered_date = %s", (pizza_ordered_date,))
    rows= cur.fetchall()
    conn.close()
    return rows

#How much they earned in total (net)

def earned_in_total(pizza_ordered_date):
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    Pizza= cur.execute("SELECT (SUM(pizza_price)) FROM pizza_itemss WHERE pizza_ordered_date = %s", (pizza_ordered_date,))
    rows_Pizza= cur.fetchall()
    
    conn.close()
    return rows_Pizza


#How much per topping was spent
def per_topping_spent(pizza_ordered_date):
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT SUM(Topping_A_price), SUM(Topping_B_price), SUM(Topping_C_price) FROM pizza_itemss WHERE pizza_ordered_date = %s", (pizza_ordered_date,))
    rows= cur.fetchall()
    conn.close()
    return rows

#If Henry was only able to sell less than 5 pizzas or less by the end of the day, it will tell him that he has failed
def count_pizzas_to_show_message(pizza_ordered_date):
    conn= psycopg2.connect("dbname='udemy_test' user= 'postgres' password= '1234' host= 'localhost' port= '5432' ")  # This to connect with liite database
    cur= conn.cursor()
    cur.execute("SELECT COUNT(pizza_types) FROM pizza_itemss WHERE pizza_ordered_date = %s", (pizza_ordered_date,))
    rows= cur.fetchall()
    conn.close()
    return rows

#create_table()
#print(earned_in_total("11/09/2020"))
