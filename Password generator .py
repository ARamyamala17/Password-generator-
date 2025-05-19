import random
import string

print("Password Generator")

# Get user preferences
length = int(input("Enter password length: "))
include_upper = input("Include uppercase letters? (y/n): ") == 'y'
include_lower = input("Include lowercase letters? (y/n): ") == 'y'
include_digits = input("Include numbers? (y/n): ") == 'y'
include_symbols = input("Include special characters? (y/n): ") == 'y'

# Create character pool based on user input
char_pool = ''
if include_upper:
    char_pool += string.ascii_uppercase
if include_lower:
    char_pool += string.ascii_lowercase
if include_digits:
    char_pool += string.digits
if include_symbols:
    char_pool += string.punctuation

if not char_pool:
    print("Error: You must select at least one character type!")
else:
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print("Generated Password:", password)
