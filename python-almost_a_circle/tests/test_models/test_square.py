#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch

class TestSquare(unittest.TestCase):
    """Unit tests for Square class."""

    def test_square(self):
        """Test Square instantiation."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_invalid_size(self):
        """Test invalid size type."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test display method."""
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 9)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 9, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        """Test update method with args."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

if __name__ == '__main__':
    unittest.main()
