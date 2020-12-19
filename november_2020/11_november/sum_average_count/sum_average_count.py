check= 1
number_list= []
sum_of_numbers=0

def BYE():
    print("Bye Bye")
    
    
def ADD():
    global sum_of_numbers
    
    user_input= int(input(("Enter the number to be added: ")))
    number_list.append(user_input)
    sum_of_numbers += user_input
    
    
def SHOW():
    if (len(number_list)>0):
        print(number_list)
    else:
        print("\n\nPlease first select option 2 \n\n")
        
def COUNT():
    global number_count

    if (len(number_list)>0):
        number_count= len(number_list)
        print(number_count)
    else:
        print("\n\nPlease first select option 2 \n\n")

def AVERAGE():
    if (len(number_list)>0): 
        average_of_numbers= sum_of_numbers/len(number_list)
        print(average_of_numbers)
    else:
        print("\n\nPlease first select option 2 \n\n")
        
while check:
    print("Enter \n 1 for BYE \n 2 for ADD \n 3 for SHOW \n 4 for COUNT \n 5 for AVERAGE" )
    user_choice= int(input("Please enter your choice : "))
    
    if (user_choice ==  1):
        check = 0
        BYE()

    elif (user_choice ==  2):
        ADD()

    elif (user_choice ==  3):
        SHOW()

    elif (user_choice ==  4):
        COUNT()

    elif (user_choice ==  5):
        AVERAGE()


    else:
        continue
