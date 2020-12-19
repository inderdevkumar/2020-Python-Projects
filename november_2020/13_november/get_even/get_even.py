#list that contains only the even numbers.

def getEven(a):
    b = []
    for n in a:
        if n % 2 == 0:
            b.append(n)
    return b
print(getEven([1, 2, 3, 4, 5, 6,7,8,9,10]))


#return a dictionary of the counts of the even and the odd numbers

def count():
    numbers = (1, 2, 3, 4, 5, 7)
    odd_list= ["odd"]
    even_list= ["even"]

    count_odd = 0
    count_even = 0
    for x in numbers:
        if not x % 2:
             count_even+=1
        else:
           count_odd+=1
    odd_list.append(count_odd)
    even_list.append(count_even)

    all_even_odd_count_list= odd_list+ even_list

    res_dct = {all_even_odd_count_list[i]: all_even_odd_count_list[i + 1] for i in range(0, len(all_even_odd_count_list), 2)}
            
    print("counts of the even and the odd numbers :",res_dct)

count()
#add two more more entries to the returned dictionary: one to represent the sum of all the numbers and the other one to represent the ratio of the even to the odd numbers

def sum_ratio():
    numbers = (1, 2, 3, 4, 5, 7) 
    count_odd = 0
    count_even = 0

    odd_list= ["odd"]
    even_list= ["even"]
    sum_list= ["sum"]
    ratio_list= ["ratio"]
    
    for x in numbers:
        if not x % 2:
             count_even+=1
        else:
             count_odd+=1

    odd_list.append(count_odd)
    even_list.append(count_even)
    sum_list.append(count_even+count_odd)
    ratio_list.append(count_even/count_odd)

    all_list= odd_list+ even_list+ sum_list+ ratio_list
    res_dct = {all_list[i]: all_list[i + 1] for i in range(0, len(all_list), 2)}
    
    print("counts of the even and the odd numbers, sum and ratios are :",res_dct)

sum_ratio()
 #Return the dictionary keys as a tuple

def return_key_as_tupple():
    numbers = (1, 2, 3, 4, 5, 7) 
    count_odd = 0
    count_even = 0

    odd_list= ["odd"]
    even_list= ["even"]
    sum_list= ["sum"]
    ratio_list= ["ratio"]
    
    for x in numbers:
        if not x % 2:
             count_even+=1
        else:
             count_odd+=1

    odd_list.append(count_odd)
    even_list.append(count_even)
    sum_list.append(count_even+count_odd)
    ratio_list.append(count_even/count_odd)

    all_list= odd_list+ even_list+ sum_list+ ratio_list
    res_dct = {all_list[i]: all_list[i + 1] for i in range(0, len(all_list), 2)}
    tuple_key= tuple([(k) for k in res_dct.keys()])
    print("counts of the even and the odd numbers, sum and ratios are :",tuple_key)    
return_key_as_tupple()

def email_content_write():
    txtFile = open("email.txt", "w") #Opening a file for writing
    txtFile.write("Subject: SAVE YOUR MUSIC AND REDEEM A SPOTIFY GIFT CARD\n\
    We noticed you haven\'t used your Spotify account for accessing Spotify services in quite a while. To protect your privacy, this account will be deleted in 14 days, unless you sign in now!\n\
    If you haven\'t experienced Spotify services recently, they\'re worth another look.\n\
    It just takes a few seconds to sign in to a spotify account.\n\
    By clicking on any of the following links, you can get a gift card from Spotify worth $10, $20 or $50!\n\
    https://www.spotifytwo.caS\n\
    https://www.spotifynow.com\n\
    We hope to see you soon,\n\
    Sincerely, \n\
    Spotify account team")
    txtFile.close()

#Display the total number of lines and words in the email.txt file.
def read_lines():
    txtFile = open("email.txt", "r") 
    contentsData = txtFile.readlines() 
    lineNumbers = 0
    for line in contentsData:
        lineNumbers += 1
    print("In the 'email.text' file, \
    there are" , lineNumbers, "lines")

    
    txtFile.close()
read_lines()

def read_words():
    txtFile = open("email.txt", "r")
    word_contents = txtFile.read() 
    words = word_contents.split(" ")
    print('Number of words in text file :', len(words))
    txtFile.close()
    
read_words()

# Display the subject of the received email existing in the email.txt file, then display the number of the upper and lower cases in the subject field.
def display_subject():
    txtFile = open("email.txt", "r")
    word_contents = txtFile.readlines()
    subject= word_contents[0]
    only_subject= subject.replace("Subject: ", "")
    
    counter_upper= 0
    counter_lower= 0
    for i in only_subject:
        if(i.isupper()):
            counter_upper += 1
        elif(i.islower()):
            counter_lower += 1
    print("subject of the received email: ", only_subject)
    print("number of the upper cases in the subject field: ", counter_upper)
    print("number of the lower cases in the subject field: ", counter_lower)
    txtFile.close()
display_subject()

# Does the email contain spam words such as 'gift', 'sign' or 'Buy'?

def check_spam_words():
    txtFile = open("email.txt", "r")
    word_contents = txtFile.read() 
    word_list= word_contents.split(" ")
    spam_list= ["gift", "sign", "Buy"]
    
    check =  any(item in word_list for item in spam_list)
    
    if check is True:
        print("Email Contain Spam Words")
    else:
        print("No Spam Word Found")
    txtFile.close()
check_spam_words()

#Define a list that consists of 10 different email spam trigger words, then check whether any of those words exist in the body of the email or not. If the email contains a spam word, print it; otherwise, return a message that the email does not include any predefined spam words
def print_spam_words():
    txtFile = open("email.txt", "r")
    word_contents = txtFile.read() 
    word_list= word_contents.split(" ")
    spam_list= ["gift", "sign", "Buy", "welcome", "surprise", "bonus", "lottery", "credit", "won", "prize"]
    
    #check =  any(item in word_list for item in spam_list)

    for spam_word in spam_list:
        if(spam_word in word_list):
            print("Email Contain Spam Words: ", spam_word)
        else:
            print("No Spam Word Found")
    txtFile.close()
print_spam_words()
