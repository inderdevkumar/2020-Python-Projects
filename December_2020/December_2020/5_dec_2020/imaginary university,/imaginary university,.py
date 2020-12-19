##In this imaginary university, an Instructor is paid $200 per teaching hour (lecture length), each course runs
##for 12 weeks, and there is a lecture very week. Write a Python script that will output the
##Instructor's name, ID, and pay at the end of the semester. Lastly, compare the average
##pay of Female instructor versus Male instructors (e.g., the average pay for a Male
##instructor is: XYZ, the average pay for a Female instructor is XYZ. (5 points)

import pandas as pd

course_df= pd.read_csv("courseTable.txt")
professor_df= pd.read_csv("ProfessorTable.txt")

print(course_df[course_df["department"]== "Engineering"])
print(course_df.head())
print(professor_df.head())
