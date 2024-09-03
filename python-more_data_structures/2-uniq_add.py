#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    :param my_list: List of integers, possibly with duplicates
    :return: Sum of all unique integers
    """
    # Convert the list to a set to remove duplicates, then sum the set
    return sum(set(my_list))
