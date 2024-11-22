#!/usr/bin/python3
"""Manual test for Rectangle TypeError exceptions."""

from models.rectangle import Rectangle

if __name__ == "__main__":
    # Test for TypeError on non-integer width
    try:
        r1 = Rectangle("1", 2)
    except TypeError as e:
        print("[TypeError] width must be an integer:", e)

    # Test for TypeError on non-integer height
    try:
        r2 = Rectangle(1, "2")
    except TypeError as e:
        print("[TypeError] height must be an integer:", e)

    # Test for TypeError on non-integer x
    try:
        r3 = Rectangle(1, 2, "3")
    except TypeError as e:
        print("[TypeError] x must be an integer:", e)

    # Test for TypeError on non-integer y
    try:
        r4 = Rectangle(1, 2, 3, "4")
    except TypeError as e:
        print("[TypeError] y must be an integer:", e)
