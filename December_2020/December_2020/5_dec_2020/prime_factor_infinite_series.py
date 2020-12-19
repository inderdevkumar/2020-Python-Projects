#=====================  Function Defination to check prime numbers=================================

def primetest(potentialprime):
    divisor = 2
    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
            break
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True

#=====================  Function Defination to Euler of n =================================
            
def pi_euler1(n):
    count = 0
    potentialprime = 3
    prime_lists= []  #To store list of prime numbers
    deno_list= []   #To store list of denominators which are closed to numerator
    product= 1
    while count < user_input_number:
        if primetest(potentialprime) == True:
            prime_lists.append(potentialprime)  #Appending prime_lists
            
            count += 1
            potentialprime += 1
        else:
            potentialprime += 1
    

    for value in prime_lists:
        
        denominator_list= [i*4 for i in range(1,n)]
        denominator= denominator_list[min(range(len(denominator_list)), key = lambda i: abs(denominator_list[i]-value))]  #Finding the denominator which is closed to numerator
        deno_list.append(denominator)   #Appending deno_list
        
        product= product*(value/denominator)  #Finding product of expression

    print("Prime Lists are: ", prime_lists)
    print("Denominator Lists are: ", deno_list)
    print(f"pi euler1 for {n} is: ", product*4)   #To get the desired output. This calculation is performed



if __name__ == "__main__":
    user_input_number= int(input("Enter the number of terms: "))
    pi_euler1(user_input_number)
