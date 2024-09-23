#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch
import os

class TestSquare(unittest.TestCase):
    """Unit tests for Square class."""

    def test_square(self):
        """Test Square(1) exists."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_invalid_size(self):
        """Test Square("1") exists."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_invalid_size_negative(self):
        """Test Square(-1) exists."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_area(self):
        """Test area() exists."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test display() exists."""
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test to_dictionary() exists."""
        s = Square(10, 2, 1, 9)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s_dict, expected_dict)

    def test_update_args(self):
        """Test update(89, 1, 2, 3) in Square exists."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists."""
        s = Square(5)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_create(self):
        """Test create(**{ 'id': 89, 'size': 1 }) in Square exists."""
        s_dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**s_dict)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file(self):
        """Test save_to_file([Square(1)]) in Square exists."""
        s1 = Square(1, 0, 0, 10)
        s2 = Square(2, 2, 2, 20)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            data = f.read()
            self.assertIn('"id": 10', data)
            self.assertIn('"size": 1', data)

    def test_save_to_file_none(self):
        """Test save_to_file(None) in Square exists."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file(self):
        """Test load_from_file() when file exists in Square exists."""
        s1 = Square(1, 0, 0, 10)
        s2 = Square(2, 2, 2, 20)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].id, 10)
        self.assertEqual(squares[1].id, 20)

    def test_load_from_file_no_file(self):
        """Test load_from_file() when file doesn't exist in Square exists."""
        # Ensure Square.json file doesn't exist
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

if __name__ == '__main__':
    unittest.main()
