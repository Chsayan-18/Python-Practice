# Print numbers from 1 to 20, but skip all numbers divisible by 3
num = 1
while num <= 20:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
        num = num + 1
        continue
    else:
        print("Count: ", num)
    num = num + 1
