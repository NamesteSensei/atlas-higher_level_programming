def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers in a list in reverse order.

    Args:
        my_list (list): A list of integers.
    """
    if my_list:
        # Iterate through the list in reverse order
        for i in my_list[::-1]:
            # Print each integer using str.format()
            print("{:d}".format(i))
