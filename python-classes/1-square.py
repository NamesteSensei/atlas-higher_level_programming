#!/usr/bin/python3
# 1-square.py
# Defines a class Square with a private instance attribute 'size'

class Square:
    def __init__(self, size):
        # Private instance attribute '__size'
        self.__size = size  # Name mangling to make 'size' private

