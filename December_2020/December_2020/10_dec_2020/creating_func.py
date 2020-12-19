l=int(input("Length : "))
w=int(input("Width : "))
r= int(input("Radius: "))
#=========== perimeter_rectangle(l,w) Function Defination ==============================
def perimeter_rectangle(l,w):
    
    perimeter=2*(l+w)
    return perimeter

#===========  area_rectangle(l,w)  Function Defination ==============================
def area_rectangle(l,w):
    
    area=l*w
    return area

#===========  area_circle(r)  Function Defination ==============================
def area_circle(r):
    
    area= float((22/7)*r*r)  #Formula to find area of circle. Also converting into float as decimal values are expected
    return round(area, 3)  #Rounding the value to 3 decimal places

print("Area of Rectangle : ",area_rectangle(l,w))  #Function Call
print("Perimeter of Rectangle : ",perimeter_rectangle(l,w)) #Function Call
print("Area of Circle : ",area_circle(r))  #Function Call
