forms = [
    {"name": "Sayan", "age": "25", "mobile": "9876543210", "email": "sayan@gmail.com"},
    {"name": "Priya123", "age": "17", "mobile": "1234abcd", "email": "priya@gmail"},
    {"name": "Ankit", "age": "61", "mobile": "1234567890", "email": "ankit@mail.com"},
    {"name": "", "age": "29", "mobile": "98765", "email": "test@domain.com"},
]
i = 1
for form in forms:
    print()
    print(f"Checking form {i}")
    i = i+1

    # Name Validation
    name = form["name"]
    if name.isalpha() and not name.strip() == " ":
        print("✅ Valid name")
        valid_name = True
    else:
        print("❌ Invalid name")
        valid_name = False
    
    # Age Validation
    age = form["age"]
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
    
    # Mobile Number Validation
    mobile = form["mobile"]
    if mobile.isdigit() and len(mobile) == 10:
        print("✅ Valid mobile number")
        valid_mobile = True
    else:
        print("❌ Invalid mobile number")
        valid_mobile = False
    
    # Email Validation
    email = form["email"]
    if "@" in email and "." in email:
        print("✅ Valid email")
        valid_email = True
    else:
        print("❌ Invalid email")
        valid_email = False
    
    # Overall Check
    if valid_email and valid_age and valid_mobile and valid_name:
        print("✅ Form Accepted")
    else:
        print("❌ Form Rejected")