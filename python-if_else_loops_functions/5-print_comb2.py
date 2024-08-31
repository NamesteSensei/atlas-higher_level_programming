#!/usr/bin/python3
# This script prints numbers from 0 to 99, formatted as specified

for number in range(100):
    if number < 99:
        print("{:02d}, ".format(number), end="")
    else:
        print("{:02d}".format(number))
