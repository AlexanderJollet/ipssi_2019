#!/usr/bin/python3

import unittest
from noel import show_noel
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_noel_2018818(self):
        self.assertEqual( show_noel(2018-8-18), "")
 
    def test_noel_2020111(self):
        self.assertEqual( show_noel(2020-11-1), "")
 
if __name__ == '__main__':
    unittest.main()
