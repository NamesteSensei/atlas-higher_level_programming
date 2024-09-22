#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def test_display(self):
        """Test the display method."""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
