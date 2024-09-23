#!/usr/bin/python3
"""Main file to test invalid Rectangle dimensions and positions."""

from models.rectangle import Rectangle

# Test 1: Rectangle(-1, 2)
try:
    r1 = Rectangle(-1, 2)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")  # Expected: ValueError for width

# Test 2: Rectangle(0, 2)
try:
    r2 = Rectangle(0, 2)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")  # Expected: ValueError for width

# Test 3: Rectangle(1, 0)
try:
    r3 = Rectangle(1, 0)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")  # Expected: ValueError for height

# Test 4: Rectangle(1, 2, -3)
try:
    r4 = Rectangle(1, 2, -3)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")  # Expected: ValueError for x

# Test 5: Rectangle(1, 2, 3, -4)
try:
    r5 = Rectangle(1, 2, 3, -4)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")  # Expected: ValueError for y
