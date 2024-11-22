#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

# Test cases for the print_square function
print_square(4)
print("")  # Empty line for separation
print_square(10)
print("")  # Empty line for separation
print_square(0)
print("")  # Empty line for separation
print_square(1)
print("")  # Empty line for separation

# Test case for error (negative size)
try:
    print_square(-1)
except Exception as e:
    print(e)

# Test case for error (non-integer size)
try:
    print_square(2.5)
except Exception as e:
    print(e)

# Test case for error (string input)
try:
    print_square("3")
except Exception as e:
    print(e)
