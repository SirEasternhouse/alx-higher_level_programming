#!/usr/bin/python3
"""Unit tests for the base of Rectangle an square classes"""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.

        It creates two Base objects for testing.
        """
        self.b1 = Base()
        self.b2 = Base(10)

    def tearDown(self):
        """
        Method called after each test method to clean up resources.

        It deletes files created during testing.
        """
        # Delete files created during testing
        try:
            os.remove('Base.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        Test the __init__ method of Base class.

        It checks if the objects are initialized with correct IDs.
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 10)

    def test_to_json_string(self):
        """Test the to_json_string method of Base class."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        test_list = [{"key1": "value1"}, {"key2": "value2"}]
        self.assertEqual(Base.to_json_string(test_list),
                '[{"key1": "value1"}, {"key2": "value2"}]'
                )

    def test_save_to_file(self):
        """Test the save_to_file method of Base class."""
        test_list = [self.b1, self.b2]
        Base.save_to_file(test_list)
        self.assertTrue(os.path.exists('Base.json'))
        with open('Base.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 10}]')

    def test_from_json_string(self):
        """test json to string"""
        json_string = '[{"key1": "value1"}, {"key2": "value2"}]'
        self.assertEqual(Base.from_json_string(json_string), [{"key1": "value1"}, {"key2": "value2"}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """checks method creates an instance with all attr set using a dict"""
        dictionary = {"id": 5}
        obj = Base.create(**dictionary)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 5)

    def test_load_from_file(self):
        """It checks if  method returns a list of instances from a JSON file"""
        self.assertEqual(Base.load_from_file(), [])
        
        test_list = [self.b1, self.b2]
        Base.save_to_file(test_list)
        loaded_list = Base.load_from_file()
        self.assertEqual(len(loaded_list), 2)
        self.assertIsInstance(loaded_list[0], Base)
        self.assertEqual(loaded_list[0].id, 1)
        self.assertIsInstance(loaded_list[1], Base)
        self.assertEqual(loaded_list[1].id, 10)


if __name__ == '__main__':
    unittest.main()
