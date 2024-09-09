#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))           # Should print 3
print(add_integer(100, -2))        # Should print 98
print(add_integer(2))              # Should print 100
print(add_integer(100.3, -2))      # Should print 98

try:
    print(add_integer(4, "School"))  # Should raise a TypeError
except Exception as e:
    print(e)

try:
    print(add_integer(None))         # Should raise a TypeError
except Exception as e:
    print(e)

try:
    print(add_integer(float('NaN'), 1))  # Should raise a ValueError
except Exception as e:
    print(e)

try:
    print(add_integer(float('inf'), 1))  # Should raise an OverflowError
except Exception as e:
    print(e)
