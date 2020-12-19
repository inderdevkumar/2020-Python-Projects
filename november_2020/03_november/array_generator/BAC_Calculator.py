# YOUR HEADER COMMENT HERE





# YOUR FUNCTIONS DEFINITIONS HERE, INCLUDING DOCUMENTATION USING DOCSTRINGS. SEE EXAMPLE BELOW:

'''

  Purpose of Function: 

  @param: name and purpose of each parameter, if any

  @return: return value, if any

'''







#driver to call and organize all other functions

if __name__ == '__main__':

  user_weight= input('Enter your weight (in lbs): ')
  if (user_weight > 0 and user_weight < 500):
      
  weight = promptForInteger(0, 500)
  print('How many minutes has it been since your last drink? ')
  duration = promptForInteger(0, 300)
  print('Enter your sex as M or F: ')
  sex = promptForMorF()
  showImpairmentChart(weight, duration, sex)
