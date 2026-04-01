# numbers = [12, 5, 9, 14, 18, 21, 25, 30]
# for i in numbers:
#     if i%3 == 0:
#         print(i)

# emails = ["test@site.com", "invalid.com", "hello@world", "data@mail.org"]
# for email in emails:
#     if "@" in email and "." in email:
#         print(email)

# sentence = "Automation testing with Python is powerful!"
# count = 0
# for char in sentence:
#     if char.lower() in "aeiou":
#         count += 1
# print(f"Total vowels = {count}")

# users = [
#     ["Amit", "27", "amit@gmail.com"],
#     ["Rina", "17", "rina.com"],
#     ["Rohit", "35", "rohit@domain"],
#     ["Anita", "23", "anita@site.com"]
# ]
# for i, user in enumerate(users, 1):
#     print(f"\nUser {i}:")
#     email = user[2]
#     age = user[1]
#     is_valid_email = "@" in email and "." in email
#     is_valid_age = 18 <= int(age) <= 60
#     if is_valid_email and is_valid_age:
#         print("✅ All data valid")
#     elif is_valid_email and not is_valid_age:
#         print("❌ Invalid age")
#     elif not is_valid_email and is_valid_age:
#         print("❌ Invalid email")
#     elif not is_valid_age and not is_valid_email:
#         print("❌ Invalid age and Invalid email")

for i in range(1, 6):
    print("*" * i)