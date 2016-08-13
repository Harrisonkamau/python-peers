import unittest

"""
Write a program that will take a string of digits and give you all the contiguous substrings of length `n` in that string.

For example, the string "49142" has the following 3-digit series:

- 491
- 914
- 142

And the following 4-digit series:

- 4914
- 9142

And if you ask for a 6-digit series from a 5-digit string, you deserve
whatever you get.

Note that these series are only required to occupy *adjacent positions*
in the input; the digits need not be *numerically consecutive*.

"""

def slices(num_string):
	# your awesome function


class SeriesTest(unittest.TestCase):
	"""Tests for the series exercise
		Implementation note:
		The slices function should raise a ValueError with a meaningful error
		message if its length argument doesn't fit the series.
	"""

    def test_slices_of_one(self):
        self.assertEqual([[0], [1], [2], [3], [4]],
                         slices("01234", 1))

    def test_slices_of_two(self):
        self.assertEqual([[9, 7], [7, 8], [8, 6], [6, 7],
                          [7, 5], [5, 6], [6, 4]],
                         slices("97867564", 2))

    def test_slices_of_three(self):
        self.assertEqual([[9, 7, 8], [7, 8, 6], [8, 6, 7],
                          [6, 7, 5], [7, 5, 6], [5, 6, 4]],
                         slices("97867564", 3))

    def test_slices_of_four(self):
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]],
                         slices("01234", 4))

    def test_slices_of_five(self):
        self.assertEqual([[0, 1, 2, 3, 4]],
                         slices("01234", 5))

    def test_overly_long_slice(self):
        with self.assertRaises(ValueError):
            slices("012", 4)

    def test_overly_short_slice(self):
        with self.assertRaises(ValueError):
            slices("01234", 0)

