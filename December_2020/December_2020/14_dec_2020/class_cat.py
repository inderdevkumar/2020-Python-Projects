
class Cat:
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight= weight

        #Raise error
        if(self.name== "" or self.age < 0 or self.weight<0):
            raise Exception("Please enter correct Data")
        

    def __str__(self):
        
        return f"{self.name} is {self.age} years old and weigh {self.weight} pounds!"

    def __eq__(self, c1, c2):

        #Logic Used
        if(c1.name == c2.name and c1.age == c2.age and c1.weight == c2.weight):
            return "Both cats are same"
        else:
            return "Cats are different"

    def is_healthy(self):
        #Logic Used
        
        if(self.weight > 15):
            return False
        elif(self.age > 10 and self.weight < 7):
            return False
        else:
            return True

c1= Cat("Stella", 5, 11.5)
print(c1)
print(c1.is_healthy())

c2= Cat("Pip", 14, 6.5)
print(c2)
print(c2.is_healthy())


print(c2.__eq__(c1,c2))
