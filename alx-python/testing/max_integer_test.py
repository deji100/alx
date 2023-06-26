#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_length_of_list(self):
        result = max_integer()
        self.assertEqual(result, None)
        self.assertIsNone(result, None)

    def test_return_value(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)
        self.assertNotEqual(result, 3)
        self.assertIsNotNone(result, 4)
    
    def test_value_instance(self):
        self.assertIsInstance(max_integer([1, 2, 3, 4]), int)
    
    def test_function_argument_type(self):
        list1 = [3, 4, 2, 6, 7]
        result = max_integer(list1)
        self.assertEqual(result, 7)
        self.assertIsInstance(list1, list)

    def test_less_than_value(self):
        list1 = [3, 4, 2, 6, 7]
        result = max_integer(list1)
        self.assertLess(result, 10)

    def test_greater_than_value(self):
        list1 = [3, 4, 2, 6, 7]
        result = max_integer(list1)
        self.assertGreater(result, 1)