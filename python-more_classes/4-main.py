#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

# Create a rectangle instance with width=2 and height=4
my_rectangle = Rectangle(2, 4)

# Print the string representation using repr()
print("String representation using repr():")
print(repr(my_rectangle))

# Use eval to recreate a new instance from repr
print("--")
new_rectangle = eval(repr(my_rectangle))

# Print details of the new rectangle to verify it's the same as the original
print("New Rectangle using repr():")
print(repr(new_rectangle))

print("--")
print(new_rectangle is my_rectangle)  # Should be False (different instances)
print(type(new_rectangle) is type(my_rectangle))  # Should be True (same class)

