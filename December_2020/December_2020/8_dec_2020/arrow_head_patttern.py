choice= 1

def generate_pattern(arrow_length):
        
        for i in range(0, arrow_length):
            for j in range(0, i + 1):
                print("*", end="")      #end="" is used to make it printed on the same line.
            print("\r")   # whatever content is there after the \r will come at the beginning of our whole string.
        for i in range(arrow_length-1, -1 , -1):
            for j in range(0, i + 1):
               print("*", end="")       #end="" is used to make it printed on the same line.
            print("\r")  # whatever content is there after the \r will come at the beginning of our whole string
            
while choice:

    print("Please enter q or Q to exit: ")
    user_input= input("Enter the max length of arrow: ")
    
    if (user_input =="q" or user_input == "Q"):
        print("See you again! Bye.")
        choice= 0
        
    else:
        arrow_length= int(user_input)
        generate_pattern(arrow_length)
