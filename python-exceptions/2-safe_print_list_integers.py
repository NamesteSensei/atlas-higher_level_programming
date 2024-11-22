#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints and counts the integers from the first x elements of my_list.

    :param my_list: List containing any type of values
    :param x: Number of elements to print
    :return: The count of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
