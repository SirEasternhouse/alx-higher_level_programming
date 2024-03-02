#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_max_integer_positive(self):
        """
        Test max_integer with a list of positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_negative(self):
        """
        Test max_integer with a list of negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_integer_mixed(self):
        """
        Test max_integer with a list of mixed positive and negative integers.
        """
        self.assertEqual(max_integer([5, -2, 7, -4, 9]), 9)

    def test_max_integer_empty_list(self):
        """
        Test max_integer with an empty list.
        """
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
