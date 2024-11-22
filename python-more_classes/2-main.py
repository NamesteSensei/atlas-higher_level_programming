#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

# Create a rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

# Modify the width and height, and print the updated results
my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
