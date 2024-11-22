#!/usr/bin/python3
Square = __import__('5-square').Square

# Test case: Square of size 3
my_square = Square(3)
my_square.my_print()

print("--")

# Test case: Modify the size to 10
my_square.size = 10
my_square.my_print()

print("--")

# Test case: Size is set to 0, should print an empty line
my_square.size = 0
my_square.my_print()

print("--")
