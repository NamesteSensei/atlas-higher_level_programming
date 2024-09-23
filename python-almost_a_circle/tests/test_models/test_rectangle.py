#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def test_rectangle(self):
        """Test Rectangle instantiation."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(5, 8, 2, 1, 99)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.id, 99)

    def test_invalid_width_type(self):
        """Test Rectangle('1', 2) raises TypeError for width being a string."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height_type(self):
        """Test Rectangle(1, '2') raises TypeError for height being a string."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x_type(self):
        """Test Rectangle(1, 2, '3') raises TypeError for x being a string."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        """Test Rectangle(1, 2, 3, '4') raises TypeError for y being a string."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    # Existing tests like test_area, test_display, test_update, etc.

if __name__ == '__main__':
    unittest.main()
