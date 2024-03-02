#!/usr/bin/python3
""" unit test for  max-integer"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        testint the max integer in a list
    """

    def test_max_integer(self):
        """
            test cases for finding max value in list
        """
        self.assertEqual(max_integer([1, 3, 5, 2]), 5)
        self.assertEqual(max_integer([-1, -3, -5, -2]), -1)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_empty_list(self):
        """
            test  for an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_invalid_input(self):
        """
            Test case: list contains non-integer elements
        """
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'c'])
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])
        with self.assertRaises(TypeError):
            max_integer([1, 2, {}])


if __name__ == '__main__':
    unittest.main()
