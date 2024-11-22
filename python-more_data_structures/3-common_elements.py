#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    :param set_1: First set of elements
    :param set_2: Second set of elements
    :return: A set of elements common to both set_1 and set_2
    """
    # Return the intersection of the two sets
    return set_1 & set_2
