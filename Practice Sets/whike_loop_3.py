# Keep asking the user to enter a number until they give you an even number.
while True:
    even = int(input("Enter an even number: "))
    if even % 2 == 0:
        print("Even number detected ✅")
        break
    else:
        print("Not an even number !!")