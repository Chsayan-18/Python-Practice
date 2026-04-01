users = [
    {"name": "Sayan", "email": "sayan@test.com", "age": "25", "mobile": "9876543210"},
    {"name": "Rita12", "email": "rita.test.com", "age": "17", "mobile": "123456"},
    {"name": "Amit", "email": "amit@domain.org", "age": "61", "mobile": "987654321a"},
    {"name": "", "email": "valid@mail.com", "age": "30", "mobile": "9999999999"}
]
i = 1
for user in users:
    print()
    print(f"Checking user {i}:")
    i += 1

    # Name Validation
    name = user["name"]
    if name.isalpha():
        print("✅ Valid name")
        valid_name = True
    else:
        print("❌ Invalid name")
        valid_name = False
    
    # Email Validation
    email = user["email"]
    if "@" in email and "." in email:
        print("✅ Valid email")
        valid_email = True
    else:
        print("❌ Invalid email")
        valid_email = False
    
    # Age Validation
    age = user["age"]
    if age.isdigit():
        age = int(age)
        if age >= 18 and age <= 60:
            print("✅ Valid age")
            valid_age = True
        else:
            print("❌ Invalid age")
            valid_age = False
    else:
        print("❌ Invalid age")
        valid_age = False
    
    # Mobile Validation
    mobile = user["mobile"]
    if mobile.isdigit() and len(mobile) == 10:
        print("✅ Valid mobile")
        valid_mobile = True
    else:
        print("❌ Invalid mobile")
        valid_mobile = False
    
    # Overall Validation
    if valid_mobile and valid_age and valid_email and valid_name:
        print("✅ User data accepted")
    else:
        print("❌ User data rejected")