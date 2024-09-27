# test_addition.py

import unittest
from add import add_positive_integers

class TestAddPositiveIntegers(unittest.TestCase):

    def test_add_two_positive_integers(self):
        self.assertEqual(add_positive_integers(2, 3), 5)
        self.assertEqual(add_positive_integers(10, 20), 30)

    def test_add_zero(self):
        with self.assertRaises(ValueError):
            add_positive_integers(0, 5)

    def test_add_negative_integer(self):
        with self.assertRaises(ValueError):
            add_positive_integers(-1, 5)
        with self.assertRaises(ValueError):
            add_positive_integers(5, -1)

if __name__ == "__main__":
    unittest.main()
