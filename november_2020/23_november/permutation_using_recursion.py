num =  int(input("Enter total number(n): "))
chosen_num= int(input("Enter the number of item chosen(r): "))

# As we know, nPr= n!/(n-r)!

diff= num - chosen_num  # (n-r)

try:

    #=========================  Function Defination  ========================================
    def numerator_factorial(n):  #To find n!
        
        if n == 1:
           return n
        elif n < 1:
           return ("NA")
        else:
           return n*numerator_factorial(n-1)
        
    def denominator_factorial(diff):   #To find (n-r)!
        
        if diff == 1:
           return diff
        elif diff < 1:
           return ("NA")
        else:
           return diff*denominator_factorial(diff-1)

    def npr():  #To find nPr= n!/(n-r)!
        
        n_factorial= numerator_factorial(num)
        difference_factorial= denominator_factorial(diff)
        print("n factorial is: ", n_factorial)
        print("n-r factorial is: ", difference_factorial)
        cal= n_factorial/ difference_factorial
        return cal

    print("nPr is: ", npr())

#Handling ValueError if r > n , n < 0, and r < 0.
    
except TypeError:  
    print("Please make sure r > n , n < 0, and r < 0")

