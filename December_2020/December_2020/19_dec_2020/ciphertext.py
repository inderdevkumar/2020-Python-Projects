#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
    result = "" 
    list_Words= ["SQL"]
    count= 0
    for index in range(len(list_Words)):
        # traverse text 
        for i in range(len(list_Words[index])): 
            char = list_Words[index][i]
            
      
            # Encrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + s-65) % 26 + 65) 
                count += 1  
            # Encrypt lowercase characters 
            else: 
                result += chr((ord(char) + s - 97) % 26 + 97) 
                count += 1   
        list_Words.append(result )
        if (count< 25):
            encrypt(list_Words[index],4)
            return list_Words
#check the above function 
text = "SQL"
s = 4
print ("Text  : " + text) 
print ("Shift : " + str(s)) 
encrypt(text,s)
