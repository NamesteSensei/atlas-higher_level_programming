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
        """Test Square instantiation."""
        s1 = Square(5)
        s2 = Square(3, 2, 1, 99)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.id, 99)

    def test_invalid_size_type(self):
        """Test Square('5') raises TypeError for size being a string."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_negative_size(self):
        """Test Square(-5) raises ValueError for negative size."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_zero_size(self):
        """Test Square(0) raises ValueError for size == 0."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_x(self):
        """Test Square(5, -1) raises ValueError for negative x."""
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_negative_y(self):
        """Test Square(5, 1, -1) raises ValueError for negative y."""
        with self.assertRaises(ValueError):
            Square(5, 1, -1)

    def test_str_method(self):
        """Test __str__() method for Square."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_area(self):
        """Test area() method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test display() method without x and y."""
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test display() method with x and y offsets."""
        s = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test to_dictionary() method for Square."""
        s = Square(10, 2, 1, 9)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 9, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        """Test update() method with args."""
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test update() method with kwargs."""
        s = Square(5)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    # Test for Square.create
    def test_create_id(self):
        """Test Square.create(**{'id': 89}) creates Square with id only."""
        square_dict = {'id': 89}
        s = Square.create(**square_dict)
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test Square.create(**{'id': 89, 'size': 1}) creates Square with id and size."""
        square_dict = {'id': 89, 'size': 1}
        s = Square.create(**square_dict)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2}) creates Square with id, size, and x."""
        square_dict = {'id': 89, 'size': 1, 'x': 2}
        s = Square.create(**square_dict)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_create_full(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3}) creates full Square."""
        square_dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**square_dict)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    # Test for save_to_file
    def test_save_to_file_none(self):
        """Test Square.save_to_file(None) saves an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test Square.save_to_file([]) saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_squares(self):
        """Test Square.save_to_file([Square(1)]) saves the square list."""
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            self.assertIn('"size": 1', file.read())

    # Test load_from_file
    def test_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file(self):
        """Test Square.load_from_file() when file exists."""
        s1 = Square(1)
        s2 = Square(2, 2, 2, 2)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].size, 1)
        self.assertEqual(squares[1].size, 2)

if __name__ == '__main__':
    unittest.main()
