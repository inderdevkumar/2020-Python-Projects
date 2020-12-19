def function1():
    n= int(input('Enter any number: '))
    if (n < 2):
        print("Plesae enter number greater than 1")

    else:
        for i in range(2, n + 1):
            
            if(n % i == 0):
                isprime = 1
                for j in range(2, (i //2 + 1)):
                    if(i % j == 0):
                        isprime = 0
                        break
                    
                if (isprime == 1):
                    print(f"{i} is a Prime factorization of {n}")
                
def function_2():
    input_file= input("Please enter the name of input txt file : ")

    with open(input_file, "r") as rfile:
        content= rfile.read()
        list_content=  content.split(".")
        my_new_list = [(str(i+1) + ": " + list_content[i]+"\n") for i in range(len(list_content)-1)]

        output_file= input("Please enter the name of output txt file : ")
        with open(output_file, "a") as wfile:

            for item in my_new_list:
                       
                wfile.write(item)
                print(item)
                
def function_3(a, b):
    
    if a< b: 
        (a,b) = (b,a)
    if(a%b) == 0:
        return b 
    else:
        return (function_3(b, a % b)) # recursion taking place

    
def function_4(disks):


    source= 'A'
    middle= 'B'
    target= 'C'

    if disks == 1:
        print(f'Move disk 1 from tower {source} to tower {target}.')
        return

    function_4(disks - 1)
    print(f'Move disk {disks} from tower {source} to tower {target}.')
    function_4(disks - 1)
 
def function_5():
    #input_file= input("Please enter the name of input txt file : ")

    with open("sample.txt", "r") as rfile:
        content= rfile.readlines()
        print("###########  Orginal content   ###########")
        print(content[0])
        new_string = ""
        for i in range(1, len(content[0]) + 1):
            new_string += content[0][len(content[0]) - i]
        print("###########  Full reversing   ###########")
        print(new_string)
      
        list_content = content[0].split()  # splitting the content on space       
        words = list(reversed(list_content))  # reversing the words using reversed() function
        print("###########  Word to word reversing   ###########")
        new_reversed_string= " ".join(words)  # joining the words
        print(new_reversed_string)   # printing

        with open("reversed.txt", "a") as wfile:
            wfile.write("Full reversing\n\n")
            wfile.write(new_string)
            wfile.write("\n\nWord to word reversing\n")
            wfile.write(new_reversed_string)
    
        
print("\n###########  The prime factorization of an integer   ###########")        
function1()  #The prime factorization of an integer, n

print("\n###########  reads lines from a file   ###########")
function_2()   #Create program that reads lines from a file........

print("\n###########  GCD  ###########")
number1 = int(input('Enter any first positive number: '))
number2 = int(input('Enter any second positive number: '))
print(function_3(number1, number2))  #gcd

print("\n###########  Tower of Hanoi  ###########")
disks = int(input('Enter number of disks: '))    #Tower of Hanoi program
function_4(disks)

print("\n###########  Reverse   ###########")
function_5()  #reverse as well as store the content from an input file to an output file.

