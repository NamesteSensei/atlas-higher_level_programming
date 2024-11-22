#!/usr/bin/python3
# This script prints the lowercase alphabet excluding 'q' and 'e'

# Use a loop to iterate over ASCII values of lowercase letters
# The chr function converts ASCII values back to characters
# Use the end='' to avoid new line after printing

for letter in range(97, 123):
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end="")
