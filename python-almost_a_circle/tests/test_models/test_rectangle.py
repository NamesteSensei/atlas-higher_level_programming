#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os

class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def test_rectangle_instantiation(self):
        """Test Rectangle instantiation."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(5, 8, 2, 1, 99)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.id, 99)

    def test_width_type_error(self):
        """Test TypeError is raised for non-integer width."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type_error(self):
        """Test TypeError is raised for non-integer height."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type_error(self):
        """Test TypeError is raised for non-integer x."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type_error(self):
        """Test TypeError is raised for non-integer y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value_error(self):
        """Test ValueError is raised for width <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_value_error(self):
        """Test ValueError is raised for height <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_value_error(self):
        """Test ValueError is raised for x < 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_value_error(self):
        """Test ValueError is raised for y < 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)

    def test_area(self):
        """Test area() method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        """Test display() method without x and y."""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test display() method with x and y."""
        r = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str_method(self):
        """Test __str__ method for Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {'id': r.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update_with_args(self):
        """Test update method with positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_kwargs(self):
        """Test update method with keyword args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    # Test for save_to_file(None)
    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None) saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test Rectangle.save_to_file([]) saves an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    # Updated test with debug print
    def test_save_to_file_with_rectangles(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)]) saves the rectangle list."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            print("File content:", content)  # Debugging output
            self.assertIn('"width": 1', content)
            self.assertIn('"width": 2', content)

    # Test load_from_file without file
    def test_load_from_file_no_file(self):
        """Test Rectangle.load_from_file() when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file(self):
        """Test Rectangle.load_from_file() when file exists."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[1].width, 2)

if __name__ == '__main__':
    unittest.main()
