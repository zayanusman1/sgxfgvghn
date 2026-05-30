student_name = input("Enter the student's name: ")
student_age = int(input("Enter the student's age: "))
student_grade = float(input("Enter the student's grade: "))
student_credits = int(input("Enter the number of credits the student has: "))

if student_age >= 18 and student_grade >= 60 and student_credits >= 120:
    print(f"{student_name} is eligible for graduation.")
else:
    print(f"{student_name} is not eligible for graduation.")
if student_age < 18:
    print(f"{student_name} is not eligible for graduation due to age.")
elif student_grade < 60:
    print(f"{student_name} is not eligible for graduation due to grade.")
elif student_credits < 120:
    print(f"{student_name} is not eligible for graduation due to insufficient credits.")