#!/usr/bin/python3
# Script to print the alphabet except 'q' and 'e' without a newline

for i in range(97, 123):  # ASCII values from 97 ('a') to 122 ('z')
    if i != 101 and i != 113:  # Skip ASCII values for 'e' (101) and 'q' (113)
        print("{}".format(chr(i)), end="")  # Print character without newline
