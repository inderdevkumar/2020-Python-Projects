
#Input:
#automobile car  manufacturer maker  children kids
#The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.

#Output:  The car maker recommends car seats for kids if the car doesn't already have one.

user_input_replacement_pairs= input("\nPlease enter the replacement pairs in above format: ")  #user input for word replacement pairs
user_input_sentence= input("\nPlease enter sentence: ")   #user input for sentence

dict_input_replacement_pairs= dict(subString.split(" ") for subString in user_input_replacement_pairs.split("  "))   #Making dictionary for word replacement pairs
list_input_sentence= list(user_input_sentence.split(" "))   #Making list of words for sentence


#=====================  Function defination ===================

def replace(list, dictionary):
    replaced_list= [dictionary.get(item, item) for item in list]   #Checking key of dictionary in list and than replacing with dictionary values. It will be a list
    out_str = " "
    return out_str.join(replaced_list)  #Getting string from list

#=================================================================
print(dict_input_replacement_pairs)
print(list_input_sentence)
print("Output:\n\n")
print(replace(list_input_sentence, dict_input_replacement_pairs))  #Function call
