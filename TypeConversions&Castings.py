# Type Conversion (Automatic Conversion)

a = 10.667 # Float value
b = 3 # int value
print(a + b) # will change it to float automatically

# Type Casting (Manual Conversion)

# a = "3.86" # String value
# b = 10.6687 # Float value
# print(a + b) # This will throw error

# To fix this we have two steps
# Step 1, we will add another variable with converted type

c = float (a)
print(c + b) # This will not throw error

# Step 2, we will change the type of variable "a" directly

a = float ("3.86") # float value
b = 10.6687 # Float value
print(a + b)