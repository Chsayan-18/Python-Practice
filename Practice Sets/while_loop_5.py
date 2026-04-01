# Keep prompting the user until they guess "rosy" correctly
# Ignore blanks or space-only input using continue
# When guessed correctly, print: "You guessed it! ✅" and exit the loop
# Make it case-insensitive (e.g., Rosy, ROSY = valid too)
while True:
    name = input("Guess the secret word for Love: ")
    if name.lower() == "rosy":
        break
    else:
        if name.strip() == "" or name.isspace():
            print("Blank name !! Re-enter the name.")
            continue
        else:
            print("Wrong guess !! Re-guess again. ")
print("You guessed it! ✅")