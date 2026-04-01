# Sum of Positive Numbers
# Stop when the user enters 0
# Ignore negative numbers using continue
# Add positive numbers only
# Print total sum after breaking
i = 1
sum = 0
while True:
    num = int(input("Enter positive numbers: "))
    if num == 0:
        break
    else:
        if num < 0:
            print("Entered Negative number !!")
            continue
        else:
            sum = sum + num
print("Sum of Positive Numbers: ", sum)