#!/usr/bin/python3

import unittest
from tree import show_tree
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_tree_1(self):
        self.assertEqual( show_tree(int(1)), "x\nx")
 
    def test_tree_2(self):
        self.assertEqual( show_tree(int(2)), ' x \nxxx\n x ')

    def test_tree_5(self):
        self.assertEqual( show_tree(int(5)), '  x  \n xxx \nxxxxx\n xxx \n xxx \n')

    def test_tree_30(self):
        self.assertEqual( show_tree(int(30)), '               x               \n              xxx              \n             xxxxx             \n            xxxxxxx            \n           xxxxxxxxx           \n          xxxxxxxxxxx          \n         xxxxxxxxxxxxx         \n        xxxxxxxxxxxxxxx        \n       xxxxxxxxxxxxxxxxx       \n      xxxxxxxxxxxxxxxxxxx      \n     xxxxxxxxxxxxxxxxxxxxx     \n    xxxxxxxxxxxxxxxxxxxxxxx    \n   xxxxxxxxxxxxxxxxxxxxxxxxx   \n  xxxxxxxxxxxxxxxxxxxxxxxxxxx  \n xxxxxxxxxxxxxxxxxxxxxxxxxxxxx \nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n              xxx              \n              xxx              \n              xxx              \n              xxx              \n              xxx              \n              xxx              \n              xxx              \n')
 
if __name__ == '__main__':
    unittest.main()