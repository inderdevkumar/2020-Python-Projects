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



import random

class Account:

  # Construct an Account object

  def __init__(self,id,balance,annualInterestRate = 8.9):

    self.id = id

    self.balance = 500

    self.annualInterestRate = annualInterestRate

 

  def getId(self):

    return self.id

 

  def getBalance(self):

    return self.balance

 

  def getAnnualInterestRate(self):

    return self.annualInterestRate

 

  def getMonthlyInterestRate(self):

    return self.annualInterestRate / 12



  def en_currency(self): # user input - currency must be USD, EUR, or CAD

    currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()

    while (currency != "USD" and currency != "EUR" and currency != "CAD"):

      currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()

    self.currency = currency

    return self.currency


  def conversion(self,amount):

    if(self.currency == "USD"):

      self.currency == amount

      return amount

    elif(self.currency == "EUR"):

      amount = float(amount/0.86)

      return amount

    elif (self.currency == "CAD"):

      amount =float(amount/1.3)

      return amount

     

 

  def deposit(self, amount,):

    self.en_currency()

    self.balance += amount

     

  def withdraw(self, amount,):

    self.en_currency()

    self.balance -= amount

     

     

 

  def getMonthlyInterest(self):

    return self.balance * self.getMonthlyInterestRate()

   

# -------------------------------------------------------------------------------------------------------------

def main():

  # This creates the account list that we would need to use 

  accounts = []

  for i in range(1000, 9999):

    account = Account(i, 0)

    accounts.append(account)



   # The While True loop helps the ATM machine function. 

  while True:

 

    # This asks for your id which is your 4 digit pin number      ---> HERE INSERT TRY:EXCEPT BLOCK FOR ACCEPTING ONLY NUMBERS

    id = int(input(" Welcome to the Bank of Shannon's Atm Machine \n Please enter your 4 -digit account's pin number to continue: "))

 

    # This is an infinite loop is for the pin(id) 4 digit pin number.   --------> THIS IS AN INFINITE LOOP, ID IS NOT BEING UPDATED (I CHANGED pin for ID)

    while id < 1000 or id > 9999:

      id = int(input("\n Your pin does not work. Please re-enter your correct pin number "))

 

    

    while True:

 

      # This displays the menu

      print("\n1: View your Current Balance \t 2:Deposit \t 3: Withdraw \t 4:Exit ")

 

      # This allows you to select your choice from the options above.

      choice = int(input(" \n Please select your choice: "))

 

      # This looks at your account object

      for acc in accounts:

        # Comparing account id

        if acc.getId() == id:

          accountObj = acc

          break

 

      # This is for viewing your account balance. 

      if choice == 1:

        # Printing balance

        print(accountObj.getBalance())



     

     

     

    # This is the Deposit option.

      elif choice == 2:

        # This will show your amount. 

        amt = float(input("\n Please enter the amount to that you would like to deposit: "))  # ---> HERE INSERT TRY:EXCEPT BLOCK FOR ACCEPTING ONLY NUMBERS

        deposit = input("Would you like to deposit this amount: Yes or No ? " + str(amt) + " ")

 

        if deposit == "Yes" or deposit == "yes":

         # This calls your deposit

         accountObj.deposit(amt);

         # This shows your new balance after the deposit. 

         print("\n Your new Updated Balance is: " + str(accountObj.getBalance()) + " ")

        else:

          print("Please login again")# I'D SUGGEST ADDING A MESSAGE

          break

 

      # This is the withdraw option.

      elif choice == 3:

        # This will show your amount

        amt = float(input("\n Please enter the amount that you would like to withdraw: ")) # ---> HERE INSERT TRY:EXCEPT BLOCK FOR ACCEPTING ONLY NUMBERS

        withdraw = input("Would you like to withdraw this amount, Yes or No ? " + str(amt) + " ")

 

        if withdraw == "Yes" or withdraw == "yes":

          print("Withdrawal Processing")  # MY WITHDRAW WAS ACCEPTED EVEN WHEN AMOUNT WAS GREATER THAN BALANCE BUT BALANCE WAS NOT UPDATED

        else:

          break

 

        if amt < accountObj.getBalance():

         # This calls your withdraw

         accountObj.withdraw(amt)

         # This displays the updated balance after your withdrawal. 

         print("\nUpdated Balance: " + str(accountObj.getBalance()) + " ")

        elif amt > accountObj.getBalance():

   

          print("\nYou can not withdraw and have insufficient funds in your account:" +str(accountObj.getBalance()))

          print("\nPlease make a deposit or you will run into overdraft fees.");

 

      

       # This is the exit menu option that shows your transaction, your transaction number and interest rates. 

      elif choice == 4:

        print("Your ATM transaction is finished.")

        print("You transaction number is : ", random.randint(10000, 1000000))

        print("Your Current Interest Rate is : ", accountObj.annualInterestRate)

        print("Your Monthly Interest Rate is: {:0.2f}".format(accountObj.annualInterestRate / 12))

        print("Thanks for choosing The Bank of Shannon as your bank. Have a nice day!!!")

        exit()         

 



main()
