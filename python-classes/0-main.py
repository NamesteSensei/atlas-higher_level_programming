#!/usr/bin/python3
# Testing the Square class from square.py

from square import Square  # Importing from the renamed file

my_square = Square()
print(type(my_square))  # Should output: <class 'square.Square'>
print(my_square.__dict__)  # Should output: {} (empty dictionary)
