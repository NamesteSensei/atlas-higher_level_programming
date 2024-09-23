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

    def test_invalid_width(self):
        """Test invalid width type."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height(self):
        """Test invalid height type."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x(self):
        """Test invalid x type."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y(self):
        """Test invalid y type."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_zero_width(self):
        """Test Rectangle(0, 2) raises ValueError for width == 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Test Rectangle(1, 0) raises ValueError for height == 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_width(self):
        """Test Rectangle(-1, 2) raises ValueError for negative width."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Test Rectangle(1, -2) raises ValueError for negative height."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_negative_x(self):
        """Test Rectangle(1, 2, -3) raises ValueError for negative x."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        """Test Rectangle(1, 2, 3, -4) raises ValueError for negative y."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        """Test display method."""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {'id': r.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        """Test update method with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

if __name__ == '__main__':
    unittest.main()
