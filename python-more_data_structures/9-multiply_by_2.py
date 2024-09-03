#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    :param a_dictionary: The original dictionary
    :return: A new dictionary with all values multiplied by 2
    """
    # Create a new dictionary with all values multiplied by 2
    return {key: value * 2 for key, value in a_dictionary.items()}
