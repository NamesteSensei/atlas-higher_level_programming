#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

