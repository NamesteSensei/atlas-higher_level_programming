#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of my_list_1 by my_list_2 up to list_length, handling
    various exceptions.

    :param my_list_1: First list (numerators)
    :param my_list_2: Second list (denominators)
    :param list_length: Number of elements to divide
    :return: A new list with division results, with 0 in case of errors
    """
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
