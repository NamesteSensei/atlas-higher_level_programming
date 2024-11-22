#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

# Create a rectangle instance with default print_symbol
my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")

# Change the print_symbol for my_rectangle_1 to "&"
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

# Create a second rectangle instance with the default print_symbol
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")

# Change the class-level print_symbol to "C"
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

# Create a third rectangle instance to test the new class-level print_symbol
my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)
print("--")

# Change the print_symbol for my_rectangle_3 to a list
my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)
print("--")
