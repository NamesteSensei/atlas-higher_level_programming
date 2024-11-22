#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

# Create a rectangle instance
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Delete the rectangle instance
del my_rectangle

# Try to access my_rectangle after deletion
try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
