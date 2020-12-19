#=============== Fruit Class   ==============================================
print("\nFruit Class:\n")

class Fruit:
    fruitcount= 0  #For fruit count
    
    def __init__(self, fruit, qty):
        self.fruit = fruit  #Getting fruit name
        self.qty = qty       #Getting fruit quantity
        
        Fruit.fruitcount= Fruit.fruitcount+ qty   #Adding fruit quantity
        
    def saysomethingGood():
        print("Fruits are good for health")
        
    def resetcount():
        Fruit.fruitcount= 0   #Resetting fruit counts


apples = Fruit("Apple", 3)
pears = Fruit("Pear", 4)
print(apples.fruit, apples.qty)
print(pears.fruit, pears.qty)
print("Total num. of fruits", Fruit.fruitcount)
Fruit.saysomethingGood()
Fruit.resetcount()
print("Total no. of fruits", Fruit.fruitcount)


#=============== Passenger Class   ==============================================
print("\nPassenger Class:\n")

class Passenger:
    count= 0    #For Passenger count
    
    def __init__(self, name, ):
        self.name = name        #Getting name of passenger
        Passenger.count= Passenger.count+ 1     #Increasing Passenger count after each name added
        
    def set_bag_weight(self, weight):
        self.weight = weight
        
    def printDetail(self):

        #==================  Checking Conditions  ==========================
        if(self.weight <= 20):
            self.bus_fare= 450
            print("Name: ", self.name)
            print(f"Bus Fare: {self.bus_fare} taka")
            
        elif(self.weight > 20 and self.weight <= 50):
            self.bus_fare= 450+ 50
            print("Name: ", self.name)
            print(f"Bus Fare: {self.bus_fare} taka")
            
        else:
            self.bus_fare= 450 + 100
            print("Name: ", self.name)
            print(f"Bus Fare: {self.bus_fare} taka")
        


print("Total passenger", Passenger.count)
p1= Passenger("Jack")
p1.set_bag_weight(90)
p2= Passenger("Carol")
p2.set_bag_weight(10)
p3= Passenger("Mike")
p3.set_bag_weight(25)
print("=============================")
p1.printDetail()
print("=============================")
p2.printDetail()
print("=============================")
p3.printDetail()
print("=============================")
print("Total Passenger", Passenger.count)
