# String methods
# Escape sequence characters --> SPecial characters used for formatting

# str1 = 'Single quoted strings'
# str2 = "Double quoted strings"
# str3 = """Triple quoted strings"""

# # Want to add "next line" in a string.

# str4 = "This is a multiple line string \nMy name is Sayan."


# # Want to add "tab space" in a string.

# str5 = "This is a multiple line string \tMy name is Sayan."

#Concatenation
# print(str1 + " " + str2)

# #Finding the length of a string using the "len(str)" function.
# print(len(str1))

#Indexing
#assigning a variable with a string.
# string = "Hello World"

# #assigning another variable with the index number [3] of the "string" variable, that is "l"
# ch = string[3]
# print(ch)

#Index_slicing (Positive --> Start with 0 from the front)
ch = "Happy Holi"
# str = ch[1:8]
# print(str)

# str1 = ch[1:] #blank end indexing means, it will continue slicing till the end of the string
# print(str1)

# str2 = ch[:9] #blank initial indexing means, it will continue slicing from the first character of the string
# print(str2)

#Index_slicing (Negetive --> Start with -1 from the extreme end of the string)
str3 = ch[-6: -1]
print(str3)