#!/usr/bin/python3
# Function to print and return the last digit of a number

def print_last_digit(number):
    # Calculate the last digit (handle negative numbers too)
    last_digit = abs(number) % 10
    # Print the last digit
    print("{}".format(last_digit), end="")
    # Return the last digit
    return last_digit
