import re 

def first_in_parens(s):

    open_bracket= s.find("(")   #To find index of ( in string
    close_bracket= s.find(")")  #To find index of ) in string
    
    bigger_substring= s[open_bracket:]   #Breaking string into two

    list_of_all= []      #List

    #==========  Logic used  ===================
    
    if ")" in bigger_substring:
        search_results = re.finditer(r'\(.*?\)', s)    #Regex used to check pair of ()
        for item in search_results: 
            substring=  item.group(0)
            list_of_all.append(substring)     #Appending into list
        print(list_of_all[0][1:-1])   #Taking only first appeared
    else:
        assert (")" in bigger_substring),"string with a matching pair of parens '()' should exist"    #Assertion used

#Used while just to test multiple entry for input strings
        
while True:
    mystring= input("Enter your string: ")
    #Function call
    first_in_parens(mystring)

