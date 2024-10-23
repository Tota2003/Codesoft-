import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Prompt user for password length
try:
    password_length = int(input("Enter the desired length of the password: "))
    if password_length < 4:
        print("Password length should be at least 4 for better security.")
    else:
        # Generate and display the password
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number for the password length.")
