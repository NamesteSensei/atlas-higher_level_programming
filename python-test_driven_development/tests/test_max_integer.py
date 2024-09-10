#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.8, 2.1]), 3.8)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == "__main__":
    unittest.main()
