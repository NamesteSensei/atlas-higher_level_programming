#!/usr/bin/python3
Square = __import__('6-square').Square

# Test case 1: Square of size 3 with default position
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

# Test case 2: Square of size 3 with position (1, 1)
my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

# Test case 3: Square of size 3 with position (3, 0)
my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
