#============== Newly added ==============
list_of_all= []
dict_all_in_one= {}

#============== New function added ==============
def allInOne(number1, number2):
        
        res = add(number1, number2)
        list_of_all.append("add")
        list_of_all.append(res)

        res = sub(number1, number2)
        list_of_all.append("sub")
        list_of_all.append(res)

        res = mult(number1, number2)
        list_of_all.append("mult")
        list_of_all.append(res)

        try:
                res = div(number1, number2)
                list_of_all.append("div")
                list_of_all.append(res)
        except ZeroDivisionError:
                res = "It is not possible to divide by zero. Thank you."
                list_of_all.append("div")
                list_of_all.append(res)
                        
        dict_all_in_one= {list_of_all[i]:list_of_all[i+1] for i in range(0, len(list_of_all), 2)}
        
        return dict_all_in_one
    
def add(x, y):
	answer = x+y
	return answer


def sub(x, y):
	answer = x - y
	return answer


def mult(x, y):
	answer = x * y
	return answer


def div(x, y):
	answer = x / y
	return answer



# Now, lets begin to test the two values for the low and high value

#============== Logic Changed ==============

def isinrange(lr, hr, number1, number2):
	if number1 <= lr or lr >= number2:
		return '\nPlease check your input values again, This may be out of working range\n\nPlease check the numbers and try again '
	elif number1 <= hr or hr >= number2:
		return '\nPlease check your input values again, This may be out of working range\n\nPlease check the numbers and try again '



def scalc(p1):
	istring = p1.split(",")
	
	if istring[2] == "+":
		res = add(int(istring[0]), int(istring[1]))
	elif istring[2] == "-":
		res = sub(int(istring[0]), int(istring[1]))
	elif istring[2] == "*":
		res = mult(int(istring[0]), int(istring[1]))
	elif istring[2] == "/":
		try:
			res = div(int(istring[0]), int(istring[1]))
		except ZeroDivisionError:
			res = "It is not possible to divide by zero. Thank you."
	return res
