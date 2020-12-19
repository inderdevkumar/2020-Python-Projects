import itertools  #itertools is a built-in module no need to install it

character_number_input= int(input("Enter the number of character you want to enter: "))  #To get input from the user how many characters he/she wants to go for

äll_charcaters= ""  # to get the string in format as in question
word= ""  #To get alphabets in a string

for i in range(character_number_input):
    charater_user_input= input("Enter the character: ")
    äll_charcaters= äll_charcaters + charater_user_input
    word= word + charater_user_input
    äll_charcaters= äll_charcaters + ","

new_charcters= äll_charcaters[:-1]   #Removing the last charcater of the string
string_format= "{" + new_charcters + "}" #Bringing in format
print("alphabets chosen are: ", string_format)

#=================================  Function Definations  =====================================================================

#To find the length of the word and also the length of the list which has all the possible combinations
def Length(user_word):
    global all_possible_combinations
    #For length of user_word
    len_word= len(user_word)
    #for length of a list - the number total combinations 
    len_list= len(all_possible_combinations)

    print("Length of word:", len_word)
    print("Length of list of combinations:", len_list)

#To check palindrome of string from the list which has  all the possible combinations
def Palindrome():
    global all_possible_combinations
    for word in all_possible_combinations:                
        if str(word) == str(word)[::-1]:
            print("The Palindrome string is: ", word)
        else:
            print("String not Palindrome is: ", word)

#To reverse the string from the list which has  all the possible combinations   
def Reverse():
    global all_possible_combinations
    for word in all_possible_combinations:
        reversed_string= str(word)[::-1]
        print(f"Reverse of {word} is: {reversed_string}")
        

#To get substring of string from the list which has  all the possible combinations
def Substring():
    global all_possible_combinations
    for word in all_possible_combinations:
        length_of_word= len(word)
        print(f"for {word} substrings are: ")
        for i in range(length_of_word):
            subtsring= word[i]
            print(subtsring)
        
#Find all possible combinations and make a list of those combinations
def permutations(user_word, step = 0):
    global all_possible_combinations
    all_possible_combinations= [''.join(p) for p in itertools.product(user_word, repeat=2)]
    return  all_possible_combinations


#Function calls
print(permutations(word))
Length(word)
Palindrome()
Reverse()
Substring()
