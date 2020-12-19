import os
import re
# Enter your code here


#For checking word with Vowels
def function(a):
    # to accept string starting with vowel 
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'  
    if(re.search(regex, a)):  
        return True
    else:
        return False


#Here string will have 2 word both should start with e
def function1(a):
    words = a.split()
    letters = [word[0] for word in words]  #creating list of first letter of each word in sentence
    new_letters= "".join(letters) #Converting list pf letters into strings
    first_letter1= new_letters[0] #Getting first character of 1st word
    first_letter2= new_letters[1]  #Getting first character of 2nd word
    
    regex= "^e"
    
    if(re.search(regex, first_letter1) and re.search(regex, first_letter2)):
        return True
    else:
        return False
    
#String should start with letter
def function2(a):
    regex= "^[a-zA-Z].*"
    if(re.search(regex, a)):  
        return True
    else:
        return False

#Making Dictionatry

def main(x):

    #captal_words= re.findall('([A-Z][a-z]+)', x)  #Making list of word starting with capital letters
    captal_words= re.findall(r'([A-Z][a-z]*)', x)
    numbers = re.findall('[0-9]+', x)  #Making list of numbers
    # using dictionary comprehension 
    # to convert lists to dictionary 
    result = {captal_words[i]: numbers[i] for i in range(len(captal_words))} 
      
    return result

if __name__ == "__main__":

#Run each function seperately to test
    
    a = input("Input (stdin): ")
##        print(function(a))
##        print(function1(a))
##        print(function2(a))
    print(main(a))


