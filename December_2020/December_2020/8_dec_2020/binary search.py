list_numbers= []
user_input_limit= int(input("Enter number of elements in the list: "))

# iterating till the range
for i in range(user_input_limit):
   elm = int(input(f"Enter Number for position {i} to be inserted: "))
   list_numbers.append(elm)  #Appending number to the list

#=============== For hardcoded check  ===================

#list_numbers = [7, 9, 14, 22, 34]
#user_number_search = 26

def findValue(list_numbers, user_number_search, low, high):

    #===================  Condition Checked =======================================

    if high >= low:
        middle = low + (high - low) // 2  #Getting position)

        if list_numbers[middle] == user_number_search:
                return middle
        elif list_numbers[middle] < user_number_search:
                return findValue(list_numbers, user_number_search, middle + 1, high)    #Function Call
        else:
                return findValue(list_numbers, user_number_search, low, middle - 1)     #Function Call

    else:
        return -1

            
choice= 1
while choice:

    print("\n######  Main Menu Option  ########\n")
    print("Please enter q or Q to exit")
    user_input= input("Enter the number to be searched: ")
        
    if (user_input == "q" or user_input == "Q"):
        print("See you again! Bye.")
        choice= 0
        
    
    else:
        user_number_search= int(user_input)
        final_pos = findValue(list_numbers, user_number_search, 0, len(list_numbers) - 1)       #Function Call
        if final_pos == -1:
            print("This item was not found in the list.")
        else:
            print(f"Your Searched number {user_number_search} is found at index {final_pos} of the list.")




        
