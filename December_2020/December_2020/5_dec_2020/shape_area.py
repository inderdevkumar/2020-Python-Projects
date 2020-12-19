import abc 
  
class Geometry(ABC): 
  
    # abstract method 
    def find_area(self): 
        pass
    def display(self): 
        pass
  
class Circle(Geometry): 
  
    # overriding abstract method 
    def find_area(self): 
        pass
    def display(self): 
        pass 
  
class Square(Geometry): 
  
    # overriding abstract method 
    def find_area(self): 
        pass
    def display(self): 
        pass 
  
class Cube(Geometry): 
  
    # overriding abstract method 
    def find_area(self): 
        pass
    def display(self): 
        pass 
  

  
# Driver code 
R = Circle() 
R.find_area()
R.display()
  
K = Square() 
K.find_area()
K.display() 
  
M = Cube() 
M.find_area()
M.display() 
  
 
