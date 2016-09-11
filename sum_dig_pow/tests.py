import unittest
from solutions import sum_dig_pow


class Tests(unittest.TestCase):

    def test_one_to_ten(self):
        self.assertEqual(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_one_to_89(self):
        self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])

    def test_ten_to_89(self):
        self.assertEqual(sum_dig_pow(10, 89), [89])

    def test_ten_to_100(self):
        self.assertEqual(sum_dig_pow(10, 100), [89])

    def test_ninety_to_100(self):
        self.assertEqual(sum_dig_pow(90, 100), [])

    def test_89_to_135(self):
        self.assertEqual(sum_dig_pow(89, 135), [89, 135])


if __name__ == '__main__':
    unittest.main()
