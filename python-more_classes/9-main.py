#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

# Create a square with side length 5
my_square = Rectangle.square(5)

# Print the area, perimeter, and string representation of the square
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
