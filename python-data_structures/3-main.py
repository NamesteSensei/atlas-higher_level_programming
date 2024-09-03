#!/usr/bin/python3
# 3-main.py

# Import the function from the other file
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

# Test the function with a sample list
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
