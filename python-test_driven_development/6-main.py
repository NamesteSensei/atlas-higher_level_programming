#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))  # Should print 4
print(max_integer([1, 3, 4, 2]))  # Should print 4
print(max_integer([]))  # Should print None
print(max_integer([-1, -2, -3, -4]))  # Should print -1
print(max_integer([3]))  # Should print 3
