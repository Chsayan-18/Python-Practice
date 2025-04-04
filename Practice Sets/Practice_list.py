#Write a program to ask the user to enter name of their 3 favourite movies, and store then in a list.

# mov1 = input("Enter the name of the first movie : ")
# mov2 = input("Enter the name of the second movie : ")
# mov3 = input("Enter the name of the third movie : ")

# list = [mov1, mov2, mov3]
# print(list)
# print(type(list))

#Write a program to check if a list contains a palindrome of elements. (Hint: use copy() method)
#A palindrome number is a number that remains the same when its digits are reversed, like 121 or 1331. 

# list = [2, 3, 4, 5, 4, 3, 2]
# list1 = list.copy()
# list1.reverse()

# if (list == list1):
#     print("This list contains a palindrome of elements")
# else:
#     print("This list doesn't contains any palindrome of elements")

#Write a program to count the number of students with the "A" grade from the following tuple

tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

#Store the above value in a list and sort them from "A" to "D"
list = list(tup)
print(list)
#print(type(list))
list.sort()
print(list)
