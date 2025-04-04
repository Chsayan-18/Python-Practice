#Conditional STatements (if - elif - else)

# name = "Sayan"
# age = 18

# if (age >= 18):
#     print(name, "is eligible for applying for the driving license")
# else:
#     print(name, "is not eligible to apply for the driving license")


#Practice Questions
# Grade students based on marks
# marks >= 90, grade = "A"
# 90 > marks >= 80, grade = "B"
# 80 > marks >= 70, grade = "C"
# 70 > marks, grade = "D"

grade = float(input("Enter the total marks (between 100) : "))

if (grade >= 90):
    print('The student has received "A" grade')
elif (grade < 90 and grade >= 80):
    print('The student has received "B" grade')
elif (grade < 80 and grade >= 70):
    print('The student has received "C" grade')
else:
    print('The student has received "D" grade')