import random
import string

# Ask the user for the password length
length = input("How long should your password be? (just type a number): ")

# Check if the input is a number
if not length.isdigit():
    print(" It is not a number!")
else:
    length = int(length)

    # What characters we'll use: letters, numbers, symbols
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_chars = letters + numbers + symbols

    # Make the password 
    password = ''
    for i in range(length):
        password += random.choice(all_chars)

    # Show the result
    print("\nNew password:")
    print(password)