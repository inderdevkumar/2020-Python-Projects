
print("************************************************************************")
print("* Welcome to the hangman game. *")
print("* Player #1 will input the target string to be guessed by player #2 *")
print("* Player #2 will then have 10 chances to guess the letters in the word.*")
print("************************************************************************")
choice= 1
while choice:

    #Input target string
    player1_input= input(" Player #1, Enter the target string to be guessed by player #2: ")

#If target string length > 6, print error message, and input target string again
    
    if (len(player1_input) < 6):
        choice=0
        pass    #To the stuff here
    else:
        print("\n\n Invalid String. Length of word should be less than 6 \n\n")
        continue

##<Initialize variables:>

guess_count = 0

solved_flag = False

print("Player #2, enter your guesses, one character at a time.")
print("You will have ten chances to guess the letters in the word.")

##Initialize matched list to all zeros (matched list length based on target string length)
hidden_word= ""  #Storing my hidden string
length_player1_input= len(player1_input)  #Find the length of player1 string

for i in range(length_player1_input):
    hidden_word += "-"  #Creating  string with underscore of the length of player1 string
print(hidden_word)

while guess_count < 10 and solved_flag == False:
    
    guess_count += 1  #Increasing the guess count
    player2_input= input(f"\nEnter guess # {guess_count} of 10: ")  #Taking input from player 2
    
    if(player2_input in player1_input):  #To check if character exist in player1 string
        
        position= player1_input.index(player2_input)  #Finding position of character in the string provided by player1
        
        hidden_word = hidden_word[:position] + player2_input + hidden_word[position+1:] #Replace charcater hidden of hidden string in the specific position of chtrcater found
        
    print(hidden_word)


    if(hidden_word == player1_input):
        solved_flag = True
        print(f"Word is: {player1_input} Congratulations")

    elif (guess_count== 10):
        print("Too Bad")

    

  


