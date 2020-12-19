#===================  Function Defination =========================================

def division():
    choice= 1
    while choice:
        try:
            user_input_number1= int(input("Enter the first number: "))   #Taking user input
            user_input_number2= int(input("Enter the second number: ")) #Taking user input
            
            if (user_input_number1 % user_input_number2 == 0):  #Checking condition
                result= int(user_input_number1/ user_input_number2)   #Finding quotient
                return result
                choice= 0
            else:
                print("\nPlease try again, as their quotient is not whole number")
                continue
        except ZeroDivisionError:   #Fixing if Denominator is zero
            print("\nDenominator should not be zero. Please try again")
            continue
print(division())
