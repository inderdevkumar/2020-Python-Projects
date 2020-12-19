from datetime import datetime, timedelta

def daysb4month(year, month):

  # If month = 2 (February), check if leap year

  if month == 2:

    if year % 400 == 0 or year % 100 == 0 or year % 4 == 0:

      return 29

    else:

      return 28

     

  # Check if month has 31 days

  elif month in [1,3,5,7,8,10,12]:

    return 31

   

  # Otherwise, month has 30 days

  else:

    return 30

   

def int_to_date(year, month, day):

  if day > daysb4month(year, month):

    month += 1

    day = 1

  elif day == 0:

    month -= 1

    day = daysb4month(year, month)

     

  if month == 13:

    year += 1

    month = 1

     

  elif month == 0:

    year -= 1

    month = 12

   

  return year, month, day

   



class Date:

  def __init__(self, year, month, day):

    self.year = year

    self.month = month

    self.day = day

        

  def __repr__(self):

    return str(self.year) + "-" + str(self.month).zfill(2) + "-" + str(self.day).zfill(2)

   

  def __str__(self):

    return str(self.year) + "/" + str(self.month).zfill(2) + "/" + str(self.day).zfill(2)

     

  def tomorrow(self):

    new_year, new_month, new_date = int_to_date(self.year, self.month, self.day + 1)

    return Date(new_year, new_month, new_date)

   

  def yesterday(self):

    new_year, new_month, new_date = int_to_date(self.year, self.month, self.day - 1)

    return Date(new_year, new_month, new_date)

     

from datetime import datetime, timedelta  

def plus_operator():
    specific_date = datetime(2020, 11, 23)  #Static date taken is: 2020-11-23
    print("Default date taken is: 2020-11-23")
    user_input_date= int(input("Enter the days to be added: "))
    new_date = (specific_date + timedelta(user_input_date)).strftime("%Y-%m-%d")  #Subtracting and than formatting
    print (new_date)

   

def minus_operator():
    specific_date = datetime(2020, 11, 23) #Static date taken is: 2020-11-23
    print("Default date taken is: 2020-11-23")
    user_input_date= int(input("Enter the days to be subtracted: "))
    new_date = (specific_date - timedelta(user_input_date)).strftime("%Y-%m-%d")  #Subtracting and than formatting
    print (new_date)



def day_of_weeks():
    specific_date = (datetime(2020, 11, 23).weekday())+1  #Getting weekday from date , plus 1 added to bring  0 as sunday
    if(specific_date== 7):
        print("Day number is : 0")
    else:
        
        print(f"Day number is : {specific_date} for '2020-11-23'" )

#https://www.coursehero.com/qa/wait/27409914/

plus_operator()
minus_operator()
day_of_weeks()
