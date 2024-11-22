#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Safely divides two integers and prints the result inside a try-except-finally block.

    :param a: First integer (numerator)
    :param b: Second integer (denominator)
    :return: The result of the division, or None if division by zero
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
