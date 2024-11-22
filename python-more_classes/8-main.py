#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

# Create two Rectangle instances
my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

# Compare the rectangles and print the result
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

# Modify my_rectangle_2's dimensions to make it larger
my_rectangle_2.width = 10
my_rectangle_2.height = 5

# Compare the rectangles again and print the result
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
