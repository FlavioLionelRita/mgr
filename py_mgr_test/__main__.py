import unittest
from py_mgr.core import *


mgr = MainManager()

class TestManager(unittest.TestCase):
    def test_loadConfig(self):        
        self.assertEqual(mgr.Type['sbyte']['precision'],8)


unittest.main()