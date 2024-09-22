#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_size(self):
        """Test the size attribute."""
        s = Square(5)
        self.assertEqual(s.size, 5)

if __name__ == '__main__':
    unittest.main()
