def create_pattern(user_input):
    
    for i in range(1, user_input+1):
        for j in range(1, user_input-i + 1):
            print( end=" ")

        for j in range(i,0, -1):
            print(j, end="")

        for j in range(2, i+1):
            print(j, end="")
        print("")



    
choice= 1

while choice:
    user_input= int(input("Enter number of lines(1 - 9): "))
    
    #Get list of category
    
    
    if (user_input >0 and user_input < 10):
        choice= 0
        create_pattern(user_input)
        
    else:
        print("Error: you must enter a value between 1 and 9. Try again.")
        continue
