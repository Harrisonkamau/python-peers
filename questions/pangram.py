# -*- coding: utf-8 -*-

import string
import unittest

# from pangram import is_pangram


"""
# Pangram

Determine if a sentence is a pangram.

Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is "The quick brown fox jumps over the lazy dog."
"""


# your function

def is_pangram(sentence):
    status = ""

    x = set(string.ascii_lowercase)-set(sentence.lower())
    print x
    if len(x) > 0:
        return False
    else:
        return True


print is_pangram('the quick brown fox jumps over the lazy dog')


# some tests
class PangramTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_pangram(''))

    def test_valid_pangram(self):
        self.assertTrue(
            is_pangram('the quick brown fox jumps over the lazy dog'))

    def test_invalid_pangram(self):
        self.assertFalse(
            is_pangram('the quick brown fish jumps over the lazy dog'))

    def test_missing_x(self):
        self.assertFalse(is_pangram('a quick movement of the enemy will '
                                    'jeopardize five gunboats'))

    def test_mixedcase_and_punctuation(self):
        self.assertTrue(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))

    def test_unchecked_german_umlaute(self):
        self.assertTrue(is_pangram('Victor jagt zwölf Boxkämpfer quer über den'
                                   ' großen Sylter Deich.'))


if __name__ == '__main__':
    unittest.main()
