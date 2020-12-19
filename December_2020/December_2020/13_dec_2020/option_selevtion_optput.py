


user_choice= int(input("Enter choice between 1 to 10: "))
if (user_choice == 1):
    phrase= input("Enter phrase: ")
    length= len(phrase)
    print("Length of Phrase etered is: ", length)

elif (user_choice == 2):
    phrase= input("Enter phrase: ")
    nth_pos= int(input("Enter the position of letter you wanted to extract: "))
    nth_letter= phrase[nth_pos-1]
    print("Length of Phrase etered is: ", nth_letter)

elif (user_choice == 3):
    phrase= input("Enter phrase: ")
    nth_pos= int(input("Enter the position of letter you wanted to extract from last: "))
    nth_letter= phrase[-nth_pos]
    print("Length of Phrase etered is: ", nth_letter)

elif (user_choice == 4):
    phrase= input("Enter phrase: ")
    n_pos= int(input("Enter the number till you wanted to extract: "))
    all_n_char= phrase[:n_pos]
    print("Length of Phrase etered is: ", all_n_char)

elif (user_choice == 5):
    phrase= input("Enter phrase: ")
    n_pos= int(input("Enter the number till you wanted to extract from end: "))
    all_n_char= phrase[-n_pos:]
    print("Length of Phrase etered is: ", all_n_char)

elif (user_choice == 6):
    phrase= input("Enter phrase: ")
    first_pos= int(input("Enter the number from where you wanted to extract: "))
    last_pos= int(input("Enter the number till where you wanted to extract: "))
    all_n_char= phrase[first_pos-1:last_pos]
    print("Length of Phrase etered is: ", all_n_char)

elif (user_choice == 7):
    phrase= input("Enter phrase: ")
    all_char= phrase[::2]
    print("Length of Phrase etered is: ", all_char)

elif (user_choice == 8):
    phrase= input("Enter phrase: ")
    reverse= phrase[::-1]
    print("Length of Phrase etered is: ", reverse)

elif (user_choice == 9):
    phrase= input("Enter phrase: ")
    all_char= phrase[::-2]
    print("Length of Phrase etered is: ", all_char)

elif (user_choice == 10):
    phrase= input("Enter phrase: ")
    all_n_pos= int(input("Enter the nth position positions you wanted extract all charcters: "))
    all_char= phrase[::all_n_pos]
    print("Length of Phrase etered is: ", all_char)

else:
    print("Invalid choice")
