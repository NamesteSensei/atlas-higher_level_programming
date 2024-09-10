#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

# Create a rectangle instance with width=2 and height=4
my_rectangle = Rectangle(2, 4)

# Print the area and perimeter of the rectangle
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Print the string representation of the rectangle using str() and repr()
print("String representation using str():")
print(str(my_rectangle))

print("String representation using repr():")
print(repr(my_rectangle))

# Modify the width and height, and print the updated results
my_rectangle.width = 10
my_rectangle.height = 3
print("--")
print("Updated Rectangle - Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("Updated Rectangle using str():")
print(str(my_rectangle))

print("Updated Rectangle using repr():")
print(repr(my_rectangle))
