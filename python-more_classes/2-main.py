#!/usr/bin/python3
# File: 2-main.py

Rectangle = __import__('2-rectangle').Rectangle

# Test case 1: Rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)
print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))

# Test case 2: Perimeter calculation with width 2 and height 4
print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.perimeter()))

# Test case 3: Rectangle with width and height 10
my_rectangle = Rectangle(10, 10)
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))

# Test case 4: Rectangle with width 10, height default
my_rectangle = Rectangle(10)
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))

# Test case 5: Rectangle with default width and height
my_rectangle = Rectangle()
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))
