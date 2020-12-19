import math  #To calculate sqrt and pow

print("Plesae enter Vertices in (x,y) format")  #Format should be as shown (x,y)

first_point= input("Enter co-ordinate for 1st vertex: ")
second_point= input("Enter co-ordinate for 2nd vertex: ")

third_point= input("Enter co-ordinate for 3rd vertex: ")
fourth_point= input("Enter co-ordinate for 4th vertex: ")

brackets_to_remove= ["(", ")"]  #To remove brackets
for c in brackets_to_remove:
        first_point = first_point.replace(c, "")
        second_point = second_point.replace(c, "")
        third_point = third_point.replace(c, "")
        fourth_point = fourth_point.replace(c, "")

#For 1st Vertex. let A
list_of_first_point_number_string= first_point.split(",")  #To seperate the string from ","
first_number_of_first_point= float(list_of_first_point_number_string[0])
second_number_of_first_point= float(list_of_first_point_number_string[1])

#For 2nd Vertex. Let B
list_of_second_point_number_string= second_point.split(",")  #To seperate the string from ","
first_number_of_second_point= float(list_of_second_point_number_string[0])
second_number_of_second_point= float(list_of_second_point_number_string[1])

#For 3rd Vertex. Let C
list_of_third_point_number_string= third_point.split(",")   #To seperate the string from ","
first_number_of_third_point= float(list_of_third_point_number_string[0])
second_number_of_third_point= float(list_of_third_point_number_string[1])

#For 4th Vertex. Let D
list_of_fourth_point_number_string= fourth_point.split(",") #To seperate the string from ","
first_number_of_fourth_point= float(list_of_fourth_point_number_string[0])
second_number_of_fourth_point= float(list_of_fourth_point_number_string[1])

#A----B

#D----C

#AB formula is sqrt(x2-x1)^2 + (y2-y1)^2)
AB_length=  math.sqrt((math.pow((first_number_of_second_point- first_number_of_first_point),2)) + (math.pow((second_number_of_second_point- second_number_of_first_point),2)))
print(AB_length)


#CD formula is sqrt(x2-x1)^2 + (y2-y1)^2)
CD_length=  math.sqrt((math.pow((first_number_of_fourth_point- first_number_of_third_point),2)) + (math.pow((second_number_of_fourth_point- second_number_of_third_point),2)))
print(CD_length)

#BC  formula is sqrt(x2-x1)^2 + (y2-y1)^2)
BC_width=  math.sqrt((math.pow((first_number_of_third_point- first_number_of_second_point),2)) + (math.pow((second_number_of_third_point- second_number_of_second_point),2)))
print(BC_width)

#AD  formula is sqrt(x2-x1)^2 + (y2-y1)^2)
AD_width=  math.sqrt((math.pow((first_number_of_fourth_point- first_number_of_first_point),2)) + (math.pow((second_number_of_fourth_point- second_number_of_first_point),2)))
print(AD_width)

if((AB_length == CD_length) and (BC_width==AD_width)):
    area_of_rectangle= (AB_length * BC_width)
    print("Area of rectangle: ", area_of_rectangle)

else:
    print("Its not a recttangle so area is 0")


