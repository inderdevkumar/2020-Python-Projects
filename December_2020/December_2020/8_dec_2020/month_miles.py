
list_month=  []
list_miles= []
choice= 1

#=========================  Function Defination ================================================================
def main_function():

    while choice:

        #======================================  Main Menu Options  =================================================
        print("**** MENU OPTIONS ****")
        print("Type P to populate miles and month name.\nType S to search for Month.\nType M to search for Month name with smallest Miles")
        print("Type L to search for Month Name with Largest Miles.\nType E to exit.")

        #Taking choice from user
        user_choice= input("Please enter your choice: ")


        #======================================   Checking conditions  ==============================
        
        if (user_choice == "P"):
            for i in range(12):
                
                user_month= input("Please enter a month name: ")
                user_miles= int(input("Please enter miles driven for the month: "))
                list_month.append(user_month)  #Appending month name to list_month
                list_miles.append(user_miles)  #Appending Miles to list_miles
                
            print(list_month)
            print(list_miles)
                
        elif (user_choice == "S"):

            month_search= input("Please enter the month name to search: ")

            if (month_search in list_month):    #Checking if month entered by user in list_month
                index= list_month.index(month_search)   #Getting index of month entered by user
                print(f"The month name is: {month_search} and the miles driven for the month is: {list_miles[index]}")  #Printing as formatted

            else:
                print("The month name not found!")

        elif (user_choice == "M"):
            print("The result for searching the smallest miles:")
            min_miles= min(list_miles)  #Getting Minimum value from list_miles
            index= list_miles.index(min_miles)  #Getting index of the minimum value found from list_miles
            
            print(f"The month name is: {list_month[index]} and the miles driven for the month is: {list_miles[index]}") #Printing as formatted
            
        elif (user_choice == "L"):
            print("The result for searching the largest miles:")
            
            max_miles= max(list_miles)  #Getting Maximum value from list_miles
            index= list_miles.index(max_miles)  #Getting index of the Maximum value found from list_miles
            
            print(f"The month name is: {list_month[index]} and the miles driven for the month is: {list_miles[index]}") #Printing as formatted
            
        elif (user_choice == "E"):
            print("Thank you for using the program.\nBye")
            break   #Breaking while loop

        else :
            print("Invalid choice. Please try again!")
            

if __name__ == "__main__":
    
    main_function()     #Function Call   
