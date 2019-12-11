#!/usr/bin/python3

import unittest
from sla import show_sla
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_99_5(self):
        self.assertEqual( show_sla(99.5), "43h 49m 48.0s")
 
    def test_99_8(self):
        self.assertEqual( show_sla(99.8), "17h 31m 55.0s")

    def test_99_99(self):
        self.assertEqual( show_sla(99.99), "0h 52m 35.0s")
 
if __name__ == '__main__':
    unittest.main()