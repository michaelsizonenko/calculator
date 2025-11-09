import unittest
from common import is_float, is_integer, is_operation

class TestCommon(unittest.TestCase):

    def test_is_float(self):
        self.assertTrue(is_float("1"))
        self.assertTrue(is_float("1.1"))
        self.assertFalse(is_float("a"))
        self.assertFalse(is_float(""))

    def test_is_integer(self):
        self.assertTrue(is_integer("1"))
        self.assertFalse(is_integer("1.1"))
        self.assertFalse(is_integer("a"))
        self.assertFalse(is_integer(""))

    def test_is_operation(self):
        self.assertTrue(is_operation("+"))
        self.assertTrue(is_operation("-"))
        self.assertTrue(is_operation("*"))
        self.assertTrue(is_operation("/"))
        self.assertFalse(is_operation("//"))
        self.assertFalse(is_operation("%"))
        self.assertFalse(is_operation("**"))
        self.assertFalse(is_operation("1"))
        self.assertFalse(is_operation("1.1"))
        self.assertFalse(is_operation("a"))
        self.assertFalse(is_operation(""))


if __name__ == "__main__":
    unittest.main()