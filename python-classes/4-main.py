#!/usr/bin/python3
Square = __import__('4-square').Square

# Create a Square instance and print its area
my_square = Square(5)
print("Area: {}".format(my_square.area()))

# Modify the size using the setter and print the updated area
my_square.size = 10
print("Area: {}".format(my_square.area()))

# Attempt to set an invalid value for size
try:
    my_square.size = -3
except Exception as e:
    print(e)

# Attempt to set size to a non-integer value
try:
    my_square.size = "3 feet"
except Exception as e:
    print(e)
