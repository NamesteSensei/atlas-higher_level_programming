"""Unit tests for Base class."""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests for Base class."""

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

if __name__ == '__main__':
    unittest.main()
