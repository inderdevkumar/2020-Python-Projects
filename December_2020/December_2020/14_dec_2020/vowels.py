# =================  Function Defination  ===========================  

def no_vowels(input_file, output_file):
    
    try:
        with open(input_file,'r') as file:    #Opening my input file in read mode
            lines= file.readlines()     #Reading contents of text as list
            my_string= ""
            
            new_string= ""
            
            for value in lines:
                my_string += value   #Appending all element of list in string

            #======= Logic Used to copy part of input file in output file   ================
            for i in my_string:

                #=================  Checking For vowels   ======================
                if (i == "a" or i == "e" or i == "i" or i == "o"  or i == "u" or 
                     i == "A" or i == "E" or i == "I" or i == "O" or i == "U" ):
                        
                    i = ""   #Replacing any vowels found with ""
                new_string += i   #Appending all characters in string

                
            with open(output_file,'a') as wfile:     #Opening a text file in append mode
                wfile.write(new_string)  #Write in output file
    except:
        print("File Not Found!")    

no_vowels("best_song.txt", "better_song.txt")     #Function Call

