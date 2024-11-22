#!/usr/bin/python3
"""Unit tests for Base class."""

import unittest
from models.base import Base
import json

class TestBase(unittest.TestCase):
    """Unit tests for Base class."""

    def test_auto_id(self):
        """Test automatic ID assignment when not provided."""
        b1 = Base()
        b2 = Base()
        b3 = Base(42)  # Custom ID
        self.assertEqual(b1.id + 1, b2.id)
        self.assertEqual(b3.id, 42)

    def test_to_json_string_none(self):
        """Test Base.to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test Base.to_json_string with a list of dictionaries."""
        dict_list = [{'id': 12}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test Base.from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string with an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test Base.from_json_string with a JSON string."""
        json_str = '[{"id": 89}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [{'id': 89}])

    def test_create(self):
        """Test Base.create method."""
        from models.rectangle import Rectangle
        r = Rectangle(3, 5, 1, 2, 99)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertEqual(r2.id, 99)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)

    def test_save_to_file_none(self):
        """Test Base.save_to_file with None."""
        from models.rectangle import Rectangle
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Base.save_to_file with an empty list."""
        from models.rectangle import Rectangle
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file_no_file(self):
        """Test Base.load_from_file when file doesn’t exist."""
        from models.rectangle import Rectangle
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

if __name__ == '__main__':
    unittest.main()
