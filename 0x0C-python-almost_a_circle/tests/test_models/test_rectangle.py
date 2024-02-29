#!/usr/bin/python3
"""Testing the rectangle class """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init(self):
        """Test if Rectangle initializes properly."""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_width_property(self):
        """Test if width property works as expected."""
        rect = Rectangle(5, 10)
        rect.width = 20
        self.assertEqual(rect.width, 20)

    def test_height_property(self):
        """Test if height property works as expected."""
        rect = Rectangle(5, 10)
        rect.height = 15
        self.assertEqual(rect.height, 15)

    def test_x_property(self):
        """Test if x property works as expected."""
        rect = Rectangle(5, 10)
        rect.x = 2
        self.assertEqual(rect.x, 2)

    def test_y_property(self):
        """Test if y property works as expected."""
        rect = Rectangle(5, 10)
        rect.y = 3
        self.assertEqual(rect.y, 3)

    def test_area(self):
        """Test if area calculation is correct."""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test if display method prints rectangle correctly."""
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch(
                'sys.stdout', new=io.StringIO()
                ) as fake_stdout:
            rect.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        """Test if update method updates attributes correctly."""
        rect = Rectangle(5, 10)
        rect.update(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

    def test_to_dictionary(self):
        """Test if to_dictionary method returns correct dictionary."""
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_str(self):
        """Test if str method returns correct string representation."""
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_str)


if __name__ == '__main__':
    unittest.main()
