#!/usr/bin/python3
# Function to print a string in uppercase
def uppercase(str):
    """Converts a string to uppercase and prints it."""
    result = ""  # Initialize an empty string to store the uppercase result
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Check if char is lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        result += char  # Append the character to the result string
    print("{}".format(result))  # Print the entire uppercase string
