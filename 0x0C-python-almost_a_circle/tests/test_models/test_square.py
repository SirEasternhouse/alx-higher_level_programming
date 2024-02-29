#!/usr/bin/python3
"""Unit tests for square class"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    A class for testing the Square class methods.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.

        It creates a Square object for testing.
        """
        self.sq = Square(5, 2, 3, 1)

    def tearDown(self):
        """
        Method called after each test method to clean up resources.
        """
        pass

    def test_init(self):
        """
        Test the __init__ method of Square class.

        It checks if the object is initialized with correct attributes.
        """
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq.width, 5)
        self.assertEqual(self.sq.height, 5)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.y, 3)

    def test_area(self):
        """
        Test the area method of Square class.

        It checks if the method calculates the area of the square correctly.
        """
        self.assertEqual(self.sq.area(), 25)

    def test_display(self):
        """
        Test the display method of Square class.

        It checks if the method prints the square correctly.
        """
        pass  # Your test for display method goes here

    def test_update(self):
        """
        Test the update method of Square class.

        It checks if the method updates the attributes of the square correctly.
        """
        self.sq.update(2, 10, 10, 1)
        self.assertEqual(self.sq.id, 2)
        self.assertEqual(self.sq.width, 10)
        self.assertEqual(self.sq.height, 10)
        self.assertEqual(self.sq.x, 1)
        self.assertEqual(self.sq.y, 3)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square class."""
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(self.sq.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the __str__ method of Square class"""
        self.assertEqual(str(self.sq), "[Square] (1) 2/3 - 5")


if __name__ == '__main__':
    unittest.main()
