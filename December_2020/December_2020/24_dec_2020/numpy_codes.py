import numpy as np


# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    ranged_array = np.arange(1,13,1)
    x= ranged_array.reshape(6,2) 


    return x
  
#print(function1())



# Task2
def function2():
    
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    ranged_array = np.arange(10,37,1)
    floattyped_array = ranged_array.astype(np.float64)  # dtype is used to print the datatype but if you want to change the integer array to floated array then astype used
    x= floattyped_array.reshape(3,3,3)

    return x
 
#print(function2())

#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    
    x = [item for list1 in a  for item in list1 if(item%5==0 and item%7==0)] #wrtie your code here
    return x
 
#print(function3())

#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    start_index= 0
    last_index= 1
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]
  
    return arr#wrtie your code here
  
#print(function4())

#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros([4, 5]).astype(np.int32)#wrtie your code here
  
    return z
#print(function5()) 

#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr = np.zeros([2, 5]).astype(np.int32)#wrtie your code here
    arr[0,4]= 10
    arr[1,2]= 20
  
    return arr

#print(function6())    
    
#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    x[x>0]= 0
    return x#write your code here

#print(function7()) 

   

#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.empty(10, dtype=np.int)
    x.fill(6)#write your code here
  
    return x.reshape(2,5)


#print(function8())  
    
#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    a = np.arange(2,101,2)
    
  
    return a

#print(function9())  
   
    
#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    brrt=  np.array([brr])
    subt = arr-brrt.T
    
  
    return subt

#print(function10())
    
    
#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    ans = [-1 if (item%2 !=0) else item for item in arr]#write your code here 
  
    return ans


#print(function11())

###task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = 1#write your code here 
  
    return arr

#print(function12())
     

#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = [item for item in arr if item>5 and item <10]#write your code here 
  
    return ans
#print(function13())


##
#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1) #write reshape code
    ans = arr.reshape(8,3)#write your code here 
  
    return ans

#print(function14())

    
#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
     #write your code here
    ans = sorted(arr, key=lambda a_entry: a_entry[1])
  
    return ans

print(function15())
 
    
###task16
##def function16():
##    #Write a NumPy program to join a sequence of arrays along depth.
##    
##    
##    x = np.array([[1], [2], [3]])
##    y = np.array([[2], [3], [4]])
##    ans = #write your code here 
##  
##    return ans
##
##
## 
##    
##    
###Task17
##def function17():
##    # replace numbers with "YES" if it divided by 3 and 5
##    # otherwise it will be replaced with "NO"
##    # Hint: np.where
##    arr = np.arange(1,10*10+1).reshape((10,10))
##    return           # Write Your Code HERE
##
##
###Excpected Out
##
##
###Task18
##def function18():
##    # count values of "students" are exist in "piaic"
##    piaic = np.arange(100)
##    students = np.array([5,20,50,200,301,7001])
##    x = # Write you code Here
##    return x
##
##
##    #Expected output: 3
##
##
### Task19
##def function19():
##    #Create variable "X" from 1,25 (both are included) range values
##    #Convert "X" variable dimension into 5 rows and 5 columns
##    #Create one more variable "W" copy of "X" 
##    #Swap "W" row and column axis (like transpose)
##    # then create variable "b" with value equal to 5
##    # Now return output as "(X*W)+b:
##
##
##    X =   # Write your code here
##    W =   # Write your code here 
##    b =   # Write your code here
##    output =    # Write your code here
##
##
##    #expected output
##
##
##
##
###Task20
##def fucntion20():
##    #apply fuction "abc" on each value of Array "X"
##    x = np.arange(1,11)
##    def xyz(x):
##        return x*2+3-2
##
##
##    return #Write your Code here
###Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])
