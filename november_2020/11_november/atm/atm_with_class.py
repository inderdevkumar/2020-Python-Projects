

class account():


    def __init__(self):
        self.balance = 500
        self.main()
        

    def main(self):

      self.repeat = "YES"

      while self.repeat == "YES":

        self.action = input("Would you like to deposit or withdraw? ").lower()

        while (self.action != "deposit" and self.action != "withdraw"):

          self.action = input("Would you like to deposit or withdraw? ").lower()



        self.currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()

        while (self.currency != "USD" and self.currency != "EUR" and self.currency != "CAD"):

          self.currency = input("Please enter the currency. It can be USD, EUR, or CAD: ").upper()



        while True: 

            try:

              self.amount = int(input("Please enter an amount: "))

              break

            except ValueError:

              print("The amount you entered is not valid. Please re-enter an amount: ")

         

        while (self.amount <= 0):

          self.amount = int(input("The amount you entered is not valid. Please re-enter an amount: "))



        if self.action == "withdraw":

          #call the withdraw function

          if self.withdraw(self.currency, self.amount) == False:

            print ("Insufficient funds!")

        elif self.action == "deposit":

          #call the deposit function

          self.deposit(self.currency, self.amount)

        else:

          print ("Please enter 'deposit' or 'withdraw': ")



        print ("Your balance is: USD", self.balance)



        self.repeat = input("Would you like to continue? YES or NO:").upper()



      print ("Goodbye!")



    def withdraw (self, currency, amount):

      global balance

      self.amount_in_USD = self.convert (self.currency, self.amount)

      if self.amount_in_USD > self.balance:

        return False

      else:

        self.balance = self.balance - self.amount_in_USD

        return True





    def deposit (self, currency, amount):

      global balance

      self.amount_in_USD = self.convert(self.currency, self.amount)

      self.balance = self.balance + self.amount_in_USD





    def convert (self, currency, amount):

      if (self.currency == "USD"):

        return self.amount

      elif (self.currency == "EUR"):

        self.amount = self.amount/0.86

        return int(self.amount)

      elif (self.currency == "CAD"):

        self.amount = self.amount/1.3

        return int(self.amount)

           
account()
