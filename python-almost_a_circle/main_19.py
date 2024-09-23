#!/usr/bin/python3
"""Main file to test Rectangle(-1, 2)"""

from models.rectangle import Rectangle

try:
    r = Rectangle(-1, 2)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")
