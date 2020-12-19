
#========== Initial phase of code shown in fun1 ================
def fun1():
    print("\n question1 pattern :\n")
    #Tring to Fix range in fun1
    
    for j in range(0,7):  #This range is wrong should be  for i in range(1, 11)  or  for i in range(0, 10)
        print("*")

#==============  Improvement of fun1 shown in fun2  ============
def fun2():
    print("\n question2 pattern :\n")
    for i in range(1, 10):  #This is again wrong
        
        for j in range(0, i):
            print("*", end= "")  #This program will simply print all * in a same line
            
#=========  Improvement of fun2 shown in fun3  =============
def fun3():
    print("\n question3 pattern :\n")
    for i in range(1, 10):  #This is again wrong      
        for j in range(0, i):
            print("*", end= "")
            print() #This program will simply print all * , each in a line
            
#=============  Improvement of fun3 shown in fun4  =============
            
def fun4():
    print("\n question4 pattern :\n")
    for i in range(1, 10):      #This is again wrong
        
        for j in range(0, i):
            print("*", end= "")
        print()         #This program will  print all *  as we are expecting for top half. Only need to change  from for i in range(1, 10) to for i in range(1, 11)  
        
#=============   Improvement of fun4 shown in fun5        ===============  
def fun5():
    print("\n question5 pattern :\n")

    #Code for top half
    for i in range(1, 11):  #Correct range is taken
        
        for j in range(0, i):
            print("*", end= "")
        print()

    #Code for bottom half
    for i in range(10, 1, -1):  # Please change from for i in range(10, 1, -1) to for i in range(10, 0, -1):   It will print as shown in bottom half 
        
        for j in range(0, i):
            print("*", end= "")
        print()

#=============   Expected Output      ===============
def required_output():
    print("\n Expected Output :\n")

    #Code for top half
    for i in range(1, 11): 
        
        for j in range(0, i):
            print("*", end= "")
        print()

    #Code for bottom half
    for i in range(10, 0, -1):  # Corrected
        
        for j in range(0, i):
            print("*", end= "")
        print()
        
if __name__ == "__main__":
    fun1()
    fun2()
    fun3()
    fun4()
    fun5()
    required_output()
