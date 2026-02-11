# Take an integer input from the user
num = int(input("Enter an integer: "))

# Check if the number is even
if num % 2 == 0:
    # If the remainder when divided by 2 is 0, it's even
    print(num, "is even.")
else:
    # Otherwise, it's odd
    print(num, "is odd.")
