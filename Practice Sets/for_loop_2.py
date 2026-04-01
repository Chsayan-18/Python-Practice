# Print all even numbers from 2 to 20 using a for loop.
# for i in range(2, 21, 2):
#     print(i)

# Print each character of the string "AUTOMATION" on a new line.
# word = "AUTOMATION"
# for char in word:
#     print(char)

# Loop through this list and print only usernames that are 6 characters or longer:
# usernames = ["sayan", "tester1", "qa", "dev123", "admin007"]
# for users in usernames:
#     if len(users) >= 6:
#         print(users)

# Loop through the list and print only emails that are valid (i.e., contain both @ and .):
emails = ["user@test.com", "admin@", "hello123.com", "test@mail.org"]
for char in emails:
      if "@" in char:
            if "." in char:
                  print(char)

# Count how many digits are in the sentence.
sentence = "My OTP is 1234 and pin is 5678"
count = 0
for char in sentence:
      if char.isdigit():
            count = count + 1
print(f"There are total {count} digits in the string")