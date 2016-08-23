# -*- coding: utf-8 -*-
"""
Find the difference between the sum of the squares and the square of the sums of the first N natural numbers.

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)**2 = 55**2 = 3025

The sum of the squares of the first ten natural numbers is,

    1**2 + 2**2 + ... + 10**2 = 385

Hence the difference between the square of the sum of the first
ten natural numbers and the sum of the squares is 2640:

    3025 - 385 = 2640

"""

import unittest


# your functions
def square_of_sum(n):


def sum_of_squares(n):


def difference(d):


class DifferenceOfSquaresTest(unittest.TestCase):

    def test_square_of_sum_5(self):
        self.assertEqual(225, square_of_sum(5))

    def test_sum_of_squares_5(self):
        self.assertEqual(55, sum_of_squares(5))

    def test_difference_5(self):
        self.assertEqual(170, difference(5))

    def test_square_of_sum_100(self):
        self.assertEqual(25502500, square_of_sum(100))

    def test_sum_of_squares_100(self):
        self.assertEqual(338350, sum_of_squares(100))

    def test_difference_100(self):
        self.assertEqual(25164150, difference(100))


if __name__ == '__main__':
    unittest.main()
