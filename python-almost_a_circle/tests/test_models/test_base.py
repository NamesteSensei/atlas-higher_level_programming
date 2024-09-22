#!/usr/bin/python3
"""Unit tests for Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_auto_id(self):
        """Test that IDs are automatically assigned."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        """Test that custom IDs are assigned correctly."""
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

if __name__ == '__main__':
    unittest.main()
