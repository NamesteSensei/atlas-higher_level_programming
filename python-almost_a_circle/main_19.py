#!/usr/bin/python3
"""Manual test for Rectangle invalid width."""

from models.rectangle import Rectangle

try:
    r = Rectangle(-1, 2)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")
