import sys

import random



#Creating header

header = "Welcome to Wheel of Fortune! Python Edition"

print(header.center(72))

print("+" * 72)

print()

print()



#Input player's name

player_name = input("Welcome to Wheel of Fortune! Enter your name: ")



#Randomly select phrase and create blank

phrase = random.choice(open('random_phrases.txt').readlines())

print(phrase)

blank = len(phrase) * '_ '



#Creating list of consonents and vowels

cs = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W","X", "Y", "Z"]

vowels = ["A", "E", "I", "O", "U"]



#Creating guesses variable

letters_guessed = []



#Creating money board

cash = 1000



# Creating function to call a consonant 

def call_consonant():

  global cash, blank

  consonant = input("Enter a consonant: ").upper()

  if consonant in letters_guessed:

    print("You already guessed the letter, ", consonant)

  elif consonant in vowels:

    print("This is not a consonant!")

  elif consonant in cs:

    if consonant in phrase.upper():

      print("Great guess!")

       

  else:

    print("INVALID INPUT")

     

# Creating function to buy a vowel 

def buy_vowel():

  global cash

  cash = cash - 50

  vowel = input("Enter a vowel: ").upper()

  if vowel in letters_guessed:

    print("You already guessed the letter, ", vowel)

  elif vowel in cs:

    print("This is not a vowel!")

  elif vowel in vowels:

    if vowel in phrase.upper():

      print("Great guess!")

    else:

      print("Letter not in phrase.")

      cash = cash - 100

    letters_guessed.append(vowel)

  else:

    print("INVALID INPUT")

     

# Creating function to solve puzzle 

def solve_puzzle():

  global cash

  global phrase

  phrase = phrase.strip()

  solve = input("SOLVE THE PUZZLE: ").upper()

  if solve == phrase.upper():

    congrats = "CONGRATULATIONS! YOU SOLVED THE PUZZLE!"

    print("YOU SOLVED THE PUZZLE!")

  else:

    cash = cash - 100



while cash > 0:

  print(player_name + ": $" + str(cash))

  print()

  print()

  print()

  print(blank.center(72))

  print("Guesses: ", letters_guessed)

  print()

  print()

  print()

   

  #Create navigation bar

  print('PICK A CHOICE '.center(72))

  print('=' * 72)

  print('1) Call A Consonant')

  print('2) Buy A Vowel')

  print('3) Solve the Puzzle')

  print('4) Exit')

  print('=' * 72)



  choice = input('Choice: ')

  if choice == '1':

    call_consonant()

    print()

  elif choice == '2':

    buy_vowel()

    print()

  elif choice == '3':

    solve_puzzle()

  elif choice == '4':

    print('Goodbye!')

    break

  else:

    print('INVALID SELECTION!!')

    print()
