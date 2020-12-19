#============== Newly imported ==============
import mini_calc_new

def calculate():
	
	try:
		lowRange = float(input("Please enter your lower range number: "))
		highRange = float(input("please enter your higher range number: "))
		number1 = float(input("Please enter the First number: "))
		number2 = float(input("Please enter the second number: "))
		operation = str(input("input your sting like this, N1,N2,Operator: "))
		lr = lowRange
		hr = highRange
	
	# This exception is purposely to detect any character that is not a number.the input is strictly numbers.
	except ValueError:
		print("You must enter a number")
	else:
		# The next exception is for the division by zero.I indicated that if there is a zero division error we should print the outcome as described below
		if number2 == 0:
			try:
				
				print("the outcome of:", number1, "+", number2, "=", mini_calc_new.add(number1, number2))
				print("the outcome of:", number1, "-", number2, "=", mini_calc_new.sub(number1, number2))
				print("the outcome of:", number1, "*", number2, "=", mini_calc_new.mult(number1, number2))
				print("the outcome of:", number1, "/", number2, "=", mini_calc_new.div(number1, number2))

				#============== Function call Changed ==============
				
				print("\nDictionary for all in one is: \n", mini_calc_new.allInOne(number1, number2))
			except ZeroDivisionError:
				print("It is not possible to divide by zero. Thank you.")
			print(mini_calc_new.scalc(operation))

			#============== Logic Changed ==============
			
		elif ((number1 >= lowRange and number1 <= highRange) and(number2 >= lowRange and number2 <= highRange)) :
			
			print("the outcome of:", number1, "+", number2, "=", mini_calc_new.add(number1, number2))
			print("the outcome of:", number1, "-", number2, "=", mini_calc_new.sub(number1, number2))
			print("the outcome of:", number1, "*", number2, "=", mini_calc_new.mult(number1, number2))
			print("the outcome of:", number1, "/", number2, "=", mini_calc_new.div(number1, number2))
			
			#============== Function call Changed ==============
			
			print("\nDictionary for all in one is: \n",mini_calc_new.allInOne(number1, number2))
			print(mini_calc_new.scalc(operation))
		
		else:			
			print(mini_calc_new.isinrange(lr,hr,number1,number2))
		again()




# Now, lets begin to test the two values for the low and high value since we created a module for it 
"""
This is the loop, Ones you wish to try different numbers, you proceed with typing in yes as described
"""

def again():
	calc_again = (input("\nDo you wish to continue? Type in Yes or No: "))
	calc_again = calc_again.lower()
	if calc_again == 'yes':
		print()
		calculate()
	elif calc_again == 'no':
		print("THANK YOU FOR USING MY CALCULATOR!!!")
	else:
		quit()


calculate()
