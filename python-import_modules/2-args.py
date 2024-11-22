#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    arg_count = len(argv)

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
