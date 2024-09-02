#!/usr/bin/python3
if __name__ == "__main__":
    # Importing the add function from add_0 module
    from add_0 import add  # "add_0" appears only once here

    # Assign values to variables
    a = 1  # a is assigned the value 1
    b = 2  # b is assigned the value 2

    # Print the result of the addition using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))  # This prints: "1 + 2 = 3"
