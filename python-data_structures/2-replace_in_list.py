#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Function that replaces an element of a list at a specific position.
    :param my_list: list to modify
    :param idx: index of the element to replace
    :param element: new element to place at the specified index
    :return: the modified list or the original list if idx is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
