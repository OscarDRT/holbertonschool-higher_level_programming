#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        self.assertAlmostEqual(max_integer([1, 3, 6, 3]), 6)
        self.assertAlmostEqual(max_integer([6]), 6)
        self.assertAlmostEqual(max_integer([1, 3, 3]), 3)
        self.assertAlmostEqual(max_integer([]), None)

    def empty_list(self):
        self.assertIsNone(max_integer([]))

    def type_error(self):
        with self.assertRaises(TypeError):
            max_integer([2, "oscar", 5])
        with self.assertRaises(TypeError):
            max_integer((2, 5))
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer("oscar")
        with self.assertRaises(TypeError):
            max_integer([1, 2.2, 1])