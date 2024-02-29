#!/usr/bin/python3
"""Unit tests for the base of Rectangle an square classes
    
    Unittest classes:
    TestBase - line 13

"""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_generation(self):
        """Test if the IDs are generated properly."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id(self):
        """Test if the custom IDs are assigned properly"""
        obj = Base(id=100)
        self.assertEqual(obj.id, 100)

    def test_id_assignment(self):
        """Test if IDs are assigned properly when provided."""
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_id_increment(self):
        """Test if the __nb_objects counter is incremented correctly."""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(id=10)
        self.assertEqual(obj3.id, 10)

if __name__ == '__main__':
    unittest.main()
