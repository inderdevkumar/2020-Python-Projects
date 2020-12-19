def getAverage(s):
    
    list_of_words= s.split(",")  #Splitting into list
    list_of_numbers= list_of_words[1:]  #Get all element of list except first element
    
    sum= 0
    for i in range(0, len(list_of_numbers)):
        
        sum = sum + int(list_of_numbers[i])  #Find sum of all elements of list
        
    average= int(sum / (len(list_of_numbers)))  #Find average
        
    return average    #Return average



#Testing function

def testGetAverage():

  print("Testing getAverage...", end="")

  assert(getAverage("john,43,0,54") == 32)

  assert(getAverage("bob,2,305,54,900,-12") == 249)

  assert(getAverage("jane,-20,100,0,27") == 26)

  assert(getAverage("jim,0,0") == 0)

  print("Passed")

  return


testGetAverage()
