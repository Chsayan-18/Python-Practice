#First lot of Practice Problems

# Write a program to input 2 numbers & print their sum

# Number1 = float(input("Enter the first number : "))
# Number2 = float(input("Enter the second number : "))
# print("You have entered", Number1, "as your first number, and", Number2, "as your second number. So the sum of these two numbers will be", Number1 + Number2)

# Write a program to input side of a square and print it's area

# Side = float(input("Enter the side dimension of the square : "))
# print("The area of the square is : ", Side ** 2)

# Write a program to input 2 floating point numbers and print their average

# Num1 = float(input("Enter the first number : "))
# Num2 = float(input("Enter the second number : "))
# Avg = (Num1 + Num2) / 2
# print("Average of both the numbers is : ", Avg)

# Write a program to input 2 integer numbers, a & b, Print TRUE if a is greater than OR equal to b. If not, print FALSE

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# Step 1 (Using If/Else statement)
if a >= b:
    print ("True")
else:
    print("False")

#Step 2
print(a>=b) #If this is true, then it will automatically print the according boolean value (True/False)