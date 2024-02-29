#!/usr/bin/python3
"""Unit tests for the base of Rectangle an square classes"""
import unittest
import os
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

    def test_to_json_string(self):
        """Test if convert list of dictionaries to JSON string"""
        data = [{'key': 'value'}, {'key': 'value'}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"key": "value"}, {"key": "value"}]')

    def test_from_json_string(self):
        """Test if converts JSON string to list of dictionaries"""
        json_string = '[{"key", "value"}, {"key": "value"}]'
        data = Base.from_json_string(json_string)

    def test_save_to_file(self):
        """"Test if save_to_file writes JSON string to file."""
        data = [{'key': 'value'}, {'key': 'value'}]
        with open(self.filename, 'w') as file:
            file.write('[{"key": "value"}, {"key": "value"}]')
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)

    def test_create(self):
        """Test if create method creates instance with attributes set."""
        dictionary = {'id': 1, 'key': 'value'}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.key, 'value')


if __name__ == '__main__':
    unittest.main()
