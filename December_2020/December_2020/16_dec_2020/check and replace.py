import re

def doit(text):      
    
    matches=re.findall(r'\"(.+?)\"',text)
    print(matches)
    new_list= [item for item in matches if len(item) == 3]
    print(new_list)
    for value in matches:
        list_words= value.split()
        print(len(list_words))
        if (len(list_words)== 3):
            print("Under if: ",len(list_words))
            for element in list_words:
                if (element.isdigit()):
                    print("Under if for digit: ",len(list_words))
                    break
                else:
                    
                    print("Under else for digit: ",len(list_words))
                    new_text= text.replace(value, "Read a book")
                    
        return new_text
     

print(doit( 'You will "Make your Bed" and "Swipe the Floor".I will "Make your Bedsss" and "Vacuum"'))
