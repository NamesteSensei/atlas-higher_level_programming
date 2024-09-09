#!/usr/bin/python3
"""
This script tests the functionality of the Square class
defined in the 0-square module.

It checks the type of a Square object and its dictionary representation.
"""

# Importing the Square class from 0-square.py
Square = __import__('0-square').Square

# Creating an instance of the Square class
mysquare = Square()

# Printing the type of the created Square object
print(type(mysquare))

# Printing the dictionary representation of the Square instance
print(mysquare.__dict__)
