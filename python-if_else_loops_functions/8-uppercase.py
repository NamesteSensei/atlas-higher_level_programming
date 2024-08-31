#!/usr/bin/python3
# Function to print a string in uppercase

def uppercase(str):
    """Converts a string to uppercase and prints it."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # Check if char is lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end="")  # Print without adding a new line
    print("")  # Print a newline at the end
