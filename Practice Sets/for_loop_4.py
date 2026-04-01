users = [
    {"username": "sayan1", "email": "sayan@gmail.com", "password": "pass@123"},
    {"username": "raj@", "email": "rajgmail.com", "password": "123456"},
    {"username": "tester3", "email": "test@qa.org", "password": "qwerty!9"},
    {"username": "dev", "email": "", "password": "admin1234"},
]
i = 1
for user in users:
    print(f"\nChecking user {i}:")
    i += 1

    # Username Validation
    if len(user["username"]) >= 6 and user["username"].isalnum():
        print("✅ Valid Username")
        valid_username = True
    else:
        print("❌ Invalid Username")
        valid_username = False

    # Email Validation
    if "@" in user["email"] and "." in user["email"] and user["email"].strip() != "":
        print("✅ Valid Email")
        valid_email = True
    else:
        print("❌ Invalid Email")
        valid_email = False

    # Password Validation
    pwd = user["password"]
    has_letter = any(char.isalpha() for char in pwd)
    has_digit = any(char.isdigit() for char in pwd)
    has_symbol = any(not char.isalnum() for char in pwd)

    if len(pwd) >= 8 and has_letter and has_digit and has_symbol:
        print("✅ Strong Password")
        valid_password = True
    else:
        print("❌ Weak Password")
        valid_password = False

    # Overall result
    if valid_username and valid_email and valid_password:
        print("✅ Registration Successful")
    else:
        print("❌ Registration Failed")