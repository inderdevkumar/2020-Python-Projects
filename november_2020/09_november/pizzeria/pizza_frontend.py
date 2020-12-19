from tkinter import*
from tkinter import ttk
import tkinter.messagebox as messagebox
import pizza_backend as backend
from datetime import datetime




root= Tk()
root.title("Pizzeria")
root.geometry("605x620")
root.configure(background= "black")

order_item= StringVar()

#==================Main Frame==========================================
MainFrame= Frame(root)
MainFrame.grid()

Top= Frame(MainFrame, width= 400, relief= RIDGE)
Top.pack(side= TOP)

MainTitle= Label(Top, font=("arial", 35, "bold"), text= "Pizzeria")
MainTitle.grid()

#================== Sub Frames ==========================================
    

Reciept_Button_Frame= Frame(MainFrame, bd= 10, width= 450, height= 500, relief= RIDGE)
Reciept_Button_Frame.pack()

OrderDetails= LabelFrame(Reciept_Button_Frame, font=("arial", 12, "bold"), bd= 4, width= 350, height= 320, relief= RIDGE)
OrderDetails.grid(row=0, column=0)

Recipt_Frame= LabelFrame(Reciept_Button_Frame, font=("arial", 12, "bold"), bd= 20, width= 350, height= 320, relief= RIDGE )
Recipt_Frame.grid(row=1, column=0)

Button_Frame= LabelFrame(Reciept_Button_Frame, font=("arial", 12, "bold"), width= 350, height= 80, relief= RIDGE )
Button_Frame.grid(row=2, column=0)

#================== Function Defination ==========================================
def order_added():
    order_added= order_item.get()
    ordered_date = datetime.now().strftime("%m/%d/%Y")
    if (order_added == "Pizza A"):
        #pizza_types, Topping_A_price, Topping_B_price, Topping_C_price, pizza_price
        backend.insert(ordered_date, order_added, 5.99, 11.99, 8.99, 30.50)
        messagebox.showinfo(title="Success: ", message="Pizza A is added...")
    elif (order_added == "Pizza B"):
        backend.insert(ordered_date, order_added, 5.99, 0, 0, 24.50)
        messagebox.showinfo(title="Success: ", message="Pizza B is added...")
    else:
        backend.insert(ordered_date, order_added, 0, 11.99, 8.99, 28.50)
        messagebox.showinfo(title="Success: ", message="Pizza C is added...")

def show_reciept():
    
    ordered_date = datetime.now().strftime("%m/%d/%Y")
    
    txt_Reciept.delete("1.0", END)
    txt_Reciept.insert(END, "\n\t\t" + "Order Details for "+ ordered_date+ "\n\n\n")
    
    #How many pizzas in total were sold for that day
    
    total_pizzas_for_that_day= backend.pizzas_in_total_for_that_day(ordered_date)
    total_sold_pizzas= total_pizzas_for_that_day[0][0]    
    txt_Reciept.insert(END, "\t" + "Total Pizza sold  "+ "\t\t\t"+ str(total_sold_pizzas)+ "\n")
    
    #How many pizzas in total were sold for that day per pizza type (see below)
    total_pizzas_for_that_day_per_pizza_type= backend.pizzas_in_total_for_that_day_per_pizza_type(ordered_date)
    
    try:
        pizza_type1= total_pizzas_for_that_day_per_pizza_type[0][0]
        pizza_qty1= total_pizzas_for_that_day_per_pizza_type[0][1]      
        txt_Reciept.insert(END, "\t" + pizza_type1 + "\t\t\t"+ str(pizza_qty1)+ "\n")
        
        pizza_type2= total_pizzas_for_that_day_per_pizza_type[1][0]
        pizza_qty2= total_pizzas_for_that_day_per_pizza_type[1][1]
        txt_Reciept.insert(END, "\t" + pizza_type2 + "\t\t\t"+ str(pizza_qty2)+ "\n")

        pizza_type3= total_pizzas_for_that_day_per_pizza_type[2][0]
        pizza_qty3= total_pizzas_for_that_day_per_pizza_type[2][1]
        txt_Reciept.insert(END, "\t" + pizza_type3 + "\t\t\t"+ str(pizza_qty3)+ "\n")
        
    except:
        pass
        
    
    
    #How much they spent in total
    total_spent= backend.spent_in_total(ordered_date)
    
    price1= total_spent[0][0]
    price2= total_spent[0][1]
    price3= total_spent[0][2]
    total_spent_in_doller= price1+ price2+ price3
    
    txt_Reciept.insert(END, "\t" + "total_spent_in_doller" + "\t\t\t"+ "$ "+ str(total_spent_in_doller)+ "\n")
    
    #How much they earned in total (net)


    Total_earned= backend.earned_in_total(ordered_date)
    total_profit_earned= Total_earned[0][0]- total_spent_in_doller
    
    txt_Reciept.insert(END, "\t" + "total profit" + "\t\t\t"+ "$ "+ str(total_profit_earned)+ "\n")
    
    txt_Reciept.insert(END, "\t" + "total Amount Earned" + "\t\t\t"+ "$ "+ str(Total_earned[0][0])+ "\n")
    
    #How much per topping was spent
    spent_per_topping= backend.per_topping_spent(ordered_date)
    
    spent_per_topping_A= spent_per_topping[0][0]
    txt_Reciept.insert(END, "\t" + "Spent in Topping A" + "\t\t\t"+ "$ "+str(spent_per_topping_A)+ "\n")
    
    spent_per_topping_B= spent_per_topping[0][1]
    txt_Reciept.insert(END, "\t" + "Spent in Topping B" + "\t\t\t"+ "$ "+str(spent_per_topping_B)+ "\n")
    
    spent_per_topping_C= spent_per_topping[0][2]
    txt_Reciept.insert(END, "\t" + "Spent in Topping C" + "\t\t\t"+ "$ "+str(spent_per_topping_C)+ "\n\n\n")
    
    #If Henry was only able to sell less than 5 pizzas or less by the end of the day, it will tell him that he has failed
    count_pizzas_to_show_message= backend.count_pizzas_to_show_message(ordered_date)
    if (count_pizzas_to_show_message[0][0] < 5):
        messagebox.showinfo(title="Warning", message="You Failed Today...")
        txt_Reciept.insert(END, "\t\t" + "You Failed Today" + "\n")
    

#============================    Widgets  ================================================================================

lbtorder= Label(OrderDetails, font=("arial", 14, "bold"), text= "Order Item ", bd=7)
lbtorder.grid(row=0, column=0, sticky=W)

cmbo_order= ttk.Combobox(OrderDetails, textvariable= order_item, state= "readonly", font= ("arial", 20, "bold"), width= 14)
cmbo_order["value"]= ("Pizza A", "Pizza B", "Pizza C")
cmbo_order.current(0)
cmbo_order.grid(row=0, column=1)


txt_Reciept= Text(Recipt_Frame, width=60, height= 20, font= ("arial", 12, "bold"))
txt_Reciept.grid(row=0, column=0)

btnreport= Button(Button_Frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 4, text= "Report", command= show_reciept).grid(row=1, column=0)

btnorder= Button(OrderDetails, padx=18, bd=7, font= ("arial", 16, "bold"), width= 4, text= "Order", command= order_added).grid(row=0, column=2)

root.mainloop()
