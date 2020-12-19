import pandas as pd
import backend

choice= 1

def ouput_format():
    #For jail
    
    #there are 2 meanings and 11 unique synonyms
    phrase_count= backend.phrase_count(user_input)
    
    sum_of_synonyms= -1
    for element in list_user_input:
        SynsetID= element[0]
        
        unique_synonyms_count= backend.unique_synonyms_count(SynsetID)
        
        #Meaning 1: lock up or confine, in or as in a jail
        view_meaning= backend.view_meaning(SynsetID)
        
        print(f"Meaning for {SynsetID}: {view_meaning} ")
        #Synset ID: 2494356
        print(f"Synset ID: {SynsetID}")
        #Synonyms:
        print(f"Synonyms: {unique_synonyms_count}")
        
        sum_of_synonyms= sum_of_synonyms + len(unique_synonyms_count)
    print(f"There are {phrase_count[0][0]} meanings and {sum_of_synonyms} unique synonyms")
    

while choice:
    user_input= input("Please enter a phrase: ")
    list_user_input= backend.view_phrase(user_input)
    if (len(list_user_input)!= 0):
       choice= 0
       ouput_format()
    else:
        print("Try Again!: ")
        continue
    
print("Done")
