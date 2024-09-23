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

    # Other tests...

    def test_display(self):
        """Test display() method without x and y."""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test display() method with x and y offsets."""
        r = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    # Additional tests for other functionalities like __str__, update, etc.
    
if __name__ == '__main__':
    unittest.main()
