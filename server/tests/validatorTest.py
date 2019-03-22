import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from validator import Validator

class TestValidator(unittest.TestCase):

    def test_wrong_start(self):
        self.assertRaises(NameError,Validator.name,'111')

    def test_banned_symbol(self):
        self.assertRaises(Exception,Validator.name,'Iuli(a')

    def test_banned_symbol2(self):
        self.assertRaises(Exception,Validator.name,'[word')

if __name__ == '__main__':
    unittest.main()