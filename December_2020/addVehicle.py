
#Function Defination

def addVehicle(value_to_pass):
    
    list_of_words= value_to_pass.split()  #Converting String into list
    
    print("\nInput String: ", value_to_pass)  
    print("\nList of Strings: ",list_of_words)

    #===================   Logic Used  ==================================================
    str1= list_of_words[0]   #Extracting value from list with index 0
    str2= list_of_words[3]+list_of_words[4]   #Extracting value from list with index 3 and 4 and that adding both
    str3= "-1"
    str4= str1[:2]  #Extracting 1st two charcaters from str1 
    Mk_Md_Y = (list_of_words[-5], list_of_words[-4], list_of_words[-3])   #Creating tuples by extracting values from list with required indexes
    SC = 0
    new_list = [ list_of_words[-6], Mk_Md_Y, list_of_words[-2],  list_of_words[-1], SC]    #Creating list by extracting values from list with required indexes
    print("\nOutput: ",str1, str2, str3, str4, new_list)  #Displaying output

        
if __name__ == "__main__":

    value_to_pass= "PC140 Paul Clover 09 29 50000 Honda Civic 2019 25642 4"   #Input string
    
    addVehicle(value_to_pass)   #Function call
