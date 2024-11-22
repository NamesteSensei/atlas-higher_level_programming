#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one of the two sets.

    :param set_1: First set of elements
    :param set_2: Second set of elements
    :return: A set of elements present in only one set
    """

    return set_1 ^ set_2
