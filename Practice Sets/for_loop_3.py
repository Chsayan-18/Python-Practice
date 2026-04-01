# Print this pattern using nested for loop:
# *
# * *
# * * *
# * * * *
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# Print following number pyramid
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# a form with 3 fields (Name, Email, Password) for 5 users.
users = 5
fields = ["Name", "Email", "Password"]
for i in range(1, users+1):
    for field in fields:
        print(f"User {i} - Field: {field}")