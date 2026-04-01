# Allow the user to enter a password.
# Password is "admin123"
# User gets only 3 attempts
# If correct, print "Login successful"
# Else after 3 wrong attempts, print "Account locked"

attempts = 1
while attempts <= 3:
    print(f"Attempts : {attempts}/3")
    pwd = input("Enter your password: ")
    if pwd == "admin123":
        print("Login successful")
        break
    else:
        if attempts <= 2:
            print("Wrong password. Enter password again")
        else:
            print("You have entered wrong password, 3 times. \nAccount is Locked !! ")
    attempts = attempts + 1