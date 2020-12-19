#Name
#program that will calculate the weekly pay for its employees.

#User Inputs
user_hours= float(input("Enter hours: "))
user_pay_rate= float(input("Enter pay rate in $: "))


#=====================    Function Defination  ==================================
def weekly_pay(hours, pay_rate): 
    total_pay= hours* pay_rate   #Formula used to calculate total pay
    tax_amount(total_pay)
    return total_pay
    
def tax_amount(total_pay):
    tax_Amount= (4.5/100)*total_pay  #Formula used to calculate tax Amount
    return tax_Amount

    
def net_pay(total_pay, tax_Amount):
    net_pay= total_pay + tax_Amount #Formula used to calculate net pay
    return net_pay
    
#==========================================================================
if __name__ == "__main__":
    #weekly_pay(user_hours, user_pay_rate)
    total_pay_var= weekly_pay(user_hours, user_pay_rate)  # weekly_pay Function call
    print(str(round(total_pay_var,2))+ " $") #Formatting the value to 2 decimal placdes

    tax_amount_var= tax_amount(total_pay_var)   #tax_amount  Function call
    print(str(round(tax_amount_var, 2))+ " $")  #Formatting the value to 2 decimal placdes

    net_pay_var= net_pay(total_pay_var, tax_amount_var)       #net_pay  Function call
    print(str(round(net_pay_var, 2))+ " $")  #Formatting the value to 2 decimal placdes
    
