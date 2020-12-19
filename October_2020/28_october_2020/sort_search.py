#Generate a list of 50,000 random integers between 1 and 100. and Print out the elapse time to search for the item
#(for both linear and binary search) or the elapse time for each sorting algorithm.


import random
import time



def binarySearch(alist, item):
    t0= time.clock()
    first = 0
    last = len(alist)-1
    found = False
    alist.sort()
    while first<=last and not found:
        pos = 0
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    t1 = time.clock()
    elapse_time= t1- t0
    return (pos, elapse_time)

def linear_search(alist, item):
    t0= time.clock()
    for i in range(len(alist)): 
  
        if (alist[i] == item):
            t1 = time.clock()
            elapse_time= t1- t0
            return (i,elapse_time)     
    return -1
    
randomlist = []

for i in range(0,50000):
    random_number = random.randint(1,100)
    randomlist.append(random_number)
    
choice= 1

while choice:
    user_input= int(input("Enter the number to search : "))   
    if user_input in randomlist:
        choice= 0
        print(f"In Binary Search element {user_input} found at index and the elapse time is: ", binarySearch(randomlist, user_input))
        print(f"In Linear Search element {user_input} found at index and the elapse time is: ", linear_search(randomlist, user_input))
       
    else:        
        continue



    
