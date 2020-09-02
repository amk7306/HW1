# Author: Abbey Kato amk7306@psu.edu

grade = input("Enter your course 1 letter grade: ")
credit = input("Enter your course 1 credit: ")
grade_average = str(grade)
credit_average = float(credit)

if grade == "A":
  grade_point = 4.0
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "A-":
  grade_point = 3.67
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "B+":
  grade_point = 3.33
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "B":
  grade_point = 3.0
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "B-":
  grade_point = 2.67
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "C+":
  grade_point = 2.33
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "C":
  grade_point = 2.0
  print(f"Grade point for course 1 is: {grade_point}")
elif grade == "D":
  grade_apoint = 1.0
  print(f"Grade point for course 1 is: {grade_point}")
else:
  grade_point = 0.0
  print(f"Grade point for course 1 is: {grade_point}")

grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
grade2_average = str(grade2)
credit2_average = float(credit2)

if grade2 =="A":
  grade_point2 = 4.0
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="A-":
  grade_point2 = 3.67
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="B+":
  grade_point2 = 3.33
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 == "B":
  grade_point2 = 3.0
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="B-":
  grade_point2 = 2.67
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 =="C+":
  grade_point2 = 2.33
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 == "C":
  grade_point2 = 2.0
  print(f"Grade point for course 1 is: {grade_point2}")
elif grade2 == "D":
  grade_point2 = 1.0
  print(f"Grade point for course 1 is: {grade_point2}")
else:
  grade_point2 = 0.0

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
grade3_average = str(grade3)
credit3_average = float(credit3)

if grade3 == "A":
  grade_point3 = 4.0
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "A-":
  grade_point3 = 3.67
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "B+" :
  grade_point3 = 3.33
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "B":
  grade_point3 = 3.0
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "B-":
  grade_point3 = 2.67
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "C+":
  grade_point3 = 2.33
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "C":
  grade_point3 = 2.0
  print(f"Grade point for course 1 is: {grade_point3}")
elif grade3 == "D":
  grade_point3 = 1.0
  print(f"Grade point for course 1 is: {grade_point3}")
else:
  grade_point3 = 0.0
  print(f"Grade point for course 1 is: {grade_point3}")
 
 
print(f"Your GPA is: {(grade_point * credit_average + grade_point2 * credit2_average + grade3_average * grade_point3 )/ (credit_average + credit2_average + credit3_average)}")