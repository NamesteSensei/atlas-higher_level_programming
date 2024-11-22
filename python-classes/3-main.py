#!/usr/bin/python3
Square = __import__('3-square').Square

# Create a Square instance with size 3 and print its area
my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

# Attempt to access the private attribute directly (should raise an error)
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

# Create another Square instance with size 5 and print its area
my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
