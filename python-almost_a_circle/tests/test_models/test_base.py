import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unit tests for Base class."""

    def test_auto_id(self):
        """Test that IDs are automatically assigned when not provided."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id + 1, b2.id)
        self.assertEqual(b2.id + 1, b3.id)

    def test_custom_id(self):
        """Test that a custom ID is assigned if provided."""
        b = Base(100)
        self.assertEqual(b.id, 100)

if __name__ == '__main__':
    unittest.main()
