#!/usr/bin/python3
"""unittests for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class for testing the Rectangle class methods.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.

        It creates a Rectangle object for testing.
        """
        self.rect = Rectangle(5, 10, 2, 3, 1)

    def test_init(self):
        """
        Test the __init__ method of Rectangle class.

        It checks if the object is initialized with correct attributes.
        """
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)
        self.assertEqual(self.rect.id, 1)

    def test_area(self):
        """
        Test the area method of Rectangle class.

        It checks if the method calculates the area correctly.
        """
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        """
        Test the display method of Rectangle class.

        It checks if the method prints the rectangle correctly.
        """
        expected_output = "\n\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update(self):
        """
        Test the update method of Rectangle class.

        It checks if the method updates attributes correctly.
        """
        self.rect.update(10, 20, 30, 40, 50)
        self.assertEqual(self.rect.id, 10)
        self.assertEqual(self.rect.width, 20)
        self.assertEqual(self.rect.height, 30)
        self.assertEqual(self.rect.x, 40)
        self.assertEqual(self.rect.y, 50)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle class."""
        self.assertEqual(self.rect.to_dictionary(), {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3})

    def test_str(self):
        """Test the __str__ method of Rectangle class."""
        self.assertEqual(str(self.rect), "[Rectangle] (1) 2/5")

if __name__ == '__main__':
    unittest.main()
