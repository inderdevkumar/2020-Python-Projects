#Function to display avg_grades 
def avg_grades(student_dicts):
    print(student_dicts)
    
student_dicts= {
"1" : {
  "name": "Olivia",
  "grade1": 40,
  "grade2": 20,
  "grade3": 30
},

"2" : {
  "name": "Oliver",
  "grade1": 60,
  "grade2": 40,
  "grade3": 20
},

"3" : {
  "name": "Sophia",
  "grade1": 100,
  "grade2": 100,
  "grade3": 100
}
}

student_avg_grade_dict= {}

#Getting key and value of student_dicts dictionary

for key, value in student_dicts.items():

    #For calculating Average for each student
    grade1= student_dicts[key]["grade1"]
    grade2= student_dicts[key]["grade2"]
    grade3= student_dicts[key]["grade3"]
    average= (grade1 + grade2 + grade3)/3    #Make sure to check number of student. Here it is 3
    student_name= student_dicts[key]["name"]

    student_avg_grade_dict[student_name]= {"average" : average}  #Makeing nested dictionary

    
avg_grades(student_avg_grade_dict)  #Calling function
