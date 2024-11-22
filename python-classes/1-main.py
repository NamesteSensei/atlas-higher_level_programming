#!/usr/bin/python3
Square = __import__('1-square').Square

#create an instance of the square class
my_square = Square(3)

# verify the type of the created object 
print(type(my_square))

# Print the dictionary of attributes (should show the mangled private attribute)
print(my_square.__dict__)  # Expected output: {'_Square__size': 3}

# Attempt to access 'size' attribute directly, which should raise an error
try:
    print(my_square.size)  # Will raise an AttributeError
except Exception as e:
    print(e)  # Expected: 'Square' object has no attribute 'size'

# Attempt to access '__size' attribute directly, which should also raise an error
try:
    print(my_square.__size)  # Will raise an AttributeError due to name mangling
except Exception as e:
    print(e)  # Expected: 'Square' object has no attribute '__size'
