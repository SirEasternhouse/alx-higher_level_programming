#!/usr/bin/python3
""" Unittests for Square square class"""
import unittest
import os
import io
import sys
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Set up test environment."""
        self.s1 = Square(5)
        self.s2 = Square(10, 2, 3, 1)

    def tearDown(self):
        """Tear down test environment."""
        del self.s1
        del self.s2

    def test_attributes(self):
        """Test if attributes are assigned correctly."""
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, None)

        self.assertEqual(self.s2.size, 10)
        self.assertEqual(self.s2.width, 10)
        self.assertEqual(self.s2.height, 10)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 3)
        self.assertEqual(self.s2.id, 1)

    def test_update(self):
        """Test if update method updates attributes correctly."""
        self.s1.update(7)
        self.assertEqual(self.s1.size, 7)
        self.assertEqual(self.s1.width, 7)
        self.assertEqual(self.s1.height, 7)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 7)

        self.s2.update(5, 3, 2, 1)
        self.assertEqual(self.s2.size, 3)
        self.assertEqual(self.s2.width, 3)
        self.assertEqual(self.s2.height, 3)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 1)
        self.assertEqual(self.s2.id, 5)

    def test_to_dictionary(self):
        """Test if to_dictionary method returns correct dictionary."""
        self.assertEqual(self.s1.to_dictionary(),
                         {'id': None, 'size': 5, 'x': 0, 'y': 0})
        self.assertEqual(self.s2.to_dictionary(),
                         {'id': 1, 'size': 10, 'x': 2, 'y': 3})

    def test_str(self):
        """Test if str method returns correct string representation."""
        self.assertEqual(str(self.s1), "[Square] (None) 0/0 - 5")
        self.assertEqual(str(self.s2), "[Square] (1) 2/3 - 10")


if __name__ == '__main__':
    unittest.main()
