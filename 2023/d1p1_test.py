import unittest

from d1p1 import *

# Tests adapted from `problem-specifications//canonical-data.json`


class D1P1Test(unittest.TestCase):
    def test_get_first_digit_case_1(self):
        self.assertEqual(get_first_digit('1abc2'), '1')

    def test_get_first_digit_case_2(self):
        self.assertEqual(get_first_digit('abc2'), '2')

    def test_get_first_digit_case_3(self):
        self.assertEqual(get_first_digit('abc'), '')

    def test_get_last_digit_case_1(self):
        self.assertEqual(get_last_digit('1abc2'), '2')

    def test_get_last_digit_case_2(self):
        self.assertEqual(get_last_digit('1abc'), '1')

    def test_get_last_digit_case_3(self):
        self.assertEqual(get_last_digit('abc'), '')

    def test_compute_test_input(self):
        self.assertEqual(compute('d1p1_test_input.txt'), 142)

if __name__ == "__main__":
    unittest.main()
