#!/usr/bin/python3
Square = __import__('4-square').Square

# Create a Square instance with size 89 and print its area
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# Update the size and print area again
my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# Try setting size to an invalid value (string)
try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
