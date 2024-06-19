#!/usr/bin/python3

"""
Unittest for the console
module
"""


import unittest
import console
from models import storage
HBNBCommand = console.HBNBCommand

class TestConsole(unittest.TestCase):
    """ Console Test class """

    def test_do_create(self):
        """ test if creat saves with the correct parameter """

        len_before = len(storage.all())
        res = HBNBCommand().do_create('State')
        len_after = len(storage.all())
        self.assertFalse(len_before == len_after + 1)

        res = HBNBCommand().do_create('State name="My_class_name"')
        new = list(storage.all().values())[-1]
        self.assertTrue(hasattr(new, "name"))

        res = HBNBCommand().do_create('Place name="My_little_house" city_id="0001"')
        new = list(storage.all().values())[-1]
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "city_id"))
        self.assertTrue(new.name == "My little house")