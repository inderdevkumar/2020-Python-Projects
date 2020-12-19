##def collatz_sequence():
##    num_seq = [i for i in range (1,4)]
##    print(num_seq)
##    number= []
##    for i in range(len(num_seq)-1):
##        if num_seq[i] < 1:
##           return []
##        while num_seq[i] > 1:
##           if num_seq[i] % 2 == 0:
##             num_seq[i] = num_seq[i] / 2
##           else:
##             num_seq[i] = 3 * num_seq[i] + 1
##        # Added line
##           number.append(num_seq[i])    
##        print(number)
##        #maximum_number = max(number)
##        #print("The maximum value this string has reached is: ", maximum_number)
##
##collatz_sequence()


##def collatz_sequence(x):
##    seq = [x]
##    print(type(x))
##    if x < 1:
##       return []
##    while x > 1:
##       if x % 2 == 0:
##         x = int(x / 2)
##       else:
##         x = int(3 * x + 1)
##       seq.append(x)    # Added line
##    return seq
##try:
##    #for n in range(1,4):
##    n = int(input("Give me a number: "))
##    while n != 1:
##        print(n)
##        n = collatz_sequence(n)
##except ValueError:
##    print('Type a number please!')



def collatz(number):
    if number % 2 == 0:
        result = number//2
        return result
    else:    
        result = 3*number + 1
        return result
try:
    for n in range(1,4):
        #n = int(input("Give me a number: "))
        while n != 1:
            print(n)
            n = collatz(n)
except ValueError:
    print('Type a number please!')
