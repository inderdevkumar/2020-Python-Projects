choice= 1

global harris_number_count, list_harris_number, flavius_sequence_count, list_flavoius_pair, index_of_max_count

#For harris_number(number) function
harris_number_count= 0
list_harris_number= []

#For flavius_sequence(number)  function
flavius_sequence_count= 0
list_flavoius_pair= []
count_list= []
            
while choice:
    
    user_number= int(input("Enter any number: "))  #Asking user for input

    if (user_number == 0 or user_number < 0):  #Checking condition
        choice= 0
        
    else:

        #Function defination for harris number
        def harris_number(number):

            global harris_number_count, list_harris_number, flavius_sequence_count, list_flavoius_pair, index_of_max_count
            
            sum_of = 0         

            #Logic used
            
            while (number != 0):  
                
                sum_of = sum_of + (number % 10) 
                number = number // 10
                
            if (user_number % sum_of == 0):
                list_harris_number.append(user_number)  #Appending all Harris number
                harris_number_count += 1   #Counting all Harris number
                return True

            else:
                return False
        

        def flavius_sequence(number):
                        
            global  flavius_sequence_count, index_of_max_count

            #Logic Used. Recursion function is used 
            if (number == 1):
                flavius_sequence_count= flavius_sequence_count + 1
                flavous_fun_return= f"({user_number},{flavius_sequence_count})"  #Getting Flavius sequences  as (n, sequence length)
                list_flavoius_pair.append(flavous_fun_return)  #Appending all Flavius sequences

                count_list.append(flavius_sequence_count)   #Appending all Flavius sequence length
                index_of_max_count= count_list.index(max(count_list))   #Finding the longest Flavius sequence as
                return
                                       
            elif (number % 2 == 0):
                flavius_sequence_count= flavius_sequence_count + 1
                flavius_sequence(int(number/2))   #Function call
                        
            else:
                flavius_sequence_count= flavius_sequence_count + 1        
                flavius_sequence(int((3*number)+1))   #Function call
                
        harris_number(user_number)    #Function call
        flavius_sequence(user_number)   #Function call


# Function defination tto display statistics  as per question

def harris_with_longest_flavious_sequence():
    
    global harris_number_count, list_harris_number, list_flavoius_pair, index_of_max_count
        
    print("the longest Flavius sequence: ", list_flavoius_pair[index_of_max_count])
    print("Total Haris Number Count: ", harris_number_count)
            
            
    print("List of Haris Numbers :", list_harris_number)
    print("List Of Flavoius sequence:", list_flavoius_pair)
   
    
harris_with_longest_flavious_sequence()   #Function call
