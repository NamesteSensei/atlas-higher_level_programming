#!/usr/bin/python3
Square = __import__('2-square').Square

# Test with valid integer size
my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

# Test with default size (0)
my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

# Test trying to access a private attribute directly
try:
    print(my_square_1.size)  # Should raise an exception
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)  # Should raise an exception
except Exception as e:
    print(e)

# Test with invalid size (non-integer)
try:
    my_square_3 = Square("3")  # Should raise a TypeError
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

# Test with invalid size (negative value)
try:
    my_square_4 = Square(-89)  # Should raise a ValueError
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

