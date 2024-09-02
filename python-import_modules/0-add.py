#!/usr/bin/python3
if __name__ == "__main__":
    # Importing the add function from add_0 module
    from add_0 import add

    # Assign values to variables
    a = 1
    b = 2

    # Print the result of the addition using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
