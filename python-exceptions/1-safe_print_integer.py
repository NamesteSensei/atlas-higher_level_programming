#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer using {:d}.format().

    :param value: The value to print
    :return: True if value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
