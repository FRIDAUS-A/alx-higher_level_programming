#!/usr/bin/python3
"""Test for the Base Class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def Test_unique(self):
        """Test that each instance as a unique id"""
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def Test_value(self):
        """Test that the id value is correctly assigned"""
        obj = Base(100)
        self.assertEqual(obj.id, 100)

    def Test_idtype(self):
        """check if the id value ia an int"""
        obj = Base()
        self.assertIsInstance(obj.id, int)

    def Test_private_instance_attribute(self):
        """check if the __nb_objects is a private instance attribute"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

if __name__ == '__main__':
    unittest.main()
