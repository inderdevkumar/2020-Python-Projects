import math


choice= ""
while (choice == ""):
    
    # Receive the input number from the user
    x = (input("\n Enter a positive number or enter return/quit: ")) # Until the user enters return

    try:
        #check the condition to quit       
        if (x == "return" or x == "quit"):
            choice= "return"
        
        else:
            # Initialize the tolerance and estimate

            tolerance = 0.000001
            estimate = 1.0
            # Perform the successive approximations
            while True:
                 estimate = (estimate + float(x) / estimate) / 2
                 difference = abs(float(x) - estimate ** 2)

                 if difference <= tolerance:

                     break
            # Output the result

            print(" The program's estimate is: ", estimate)

            print(" Python's estimate is: ", math.sqrt(float(x)))

            print(" Your entered positive number is: ", x)
            
            continue
    except:
        print(" Not a valid number to get square root\n\n")
        pass


