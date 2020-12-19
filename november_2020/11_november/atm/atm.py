balance = 500

def main():

  repeat = "YES"

  while repeat == "YES":

    action = input("Would you like to deposit or withdraw? ").lower()

    while (action != "deposit" and action != "withdraw"):

      action = input("Would you like to deposit or withdraw? ").lower()



    currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()

    while (currency != "USD" and currency != "EUR" and currency != "CAD"):

      currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()



    while True: 

        try:

          amount = int(input("Please enter an amount: "))

          break

        except ValueError:

          print("The amount you entered is not valid. Please re-enter an amount: ")

     

    while (amount <= 0):

      amount = int(input("The amount you entered is not valid. Please re-enter an amount: "))



    if action == "withdraw":

      #call the withdraw function

      if withdraw(currency, amount) == False:

        print ("Insufficient funds!")

    elif action == "deposit":

      #call the deposit function

      deposit(currency, amount)

    else:

      print ("Please enter 'deposit' or 'withdraw': ")



    print ("Your balance is: USD", balance)



    repeat = input("Would you like to continue? YES or NO:").upper()



  print ("Goodbye!")



def withdraw (c, a):

  global balance

  amount_in_USD = convert (c, a)

  if amount_in_USD > balance:

    return False

  else:

    balance = balance - amount_in_USD

    return True





def deposit (c, a):

  global balance

  amount_in_USD = convert (c, a)

  balance = balance + amount_in_USD





def convert (c, a):

  if (c == "USD"):

    return a

  elif (c == "EUR"):

    a = a/0.86

    return int(a)

  elif (c == "CAD"):

    a = a/1.3

    return int(a)

       

main()
