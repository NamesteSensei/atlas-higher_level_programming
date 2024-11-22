#!/usr/bin/python3
# This script prints all possible different combinations of two digits

for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 < 8 or digit2 < 9:
            print("{:02d}, ".format(digit1 * 10 + digit2), end="")
        else:
            print("{:02d}".format(digit1 * 10 + digit2))
