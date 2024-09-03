#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Function that retrieves an element from a list.
    :param my_list: list from which to retrieve the element
    :param idx: index of the element to retrieve
    :return: the element at the specified index, or None if index is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
