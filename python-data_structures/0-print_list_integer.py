#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Function that prints each integer in the list on a new line.
    :param my_list: list of integers to print
    """
    for i in my_list:
        # Print the integer using str.format() without casting
        print("{:d}".format(i))
