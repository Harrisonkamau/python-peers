
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

"""
# Run Length Encoding

Implement run-length encoding and decoding.

Run-length encoding (RLE) is a simple form of data compression, where runs
(consecutive data elements) are replaced by just one data value and count.

For example we can represent the original 53 characters with only 13.

```
"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
```

RLE allows the original data to be perfectly reconstructed from
the compressed data, which makes it a lossless data compression.

```
"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
```
"""


def encode(s_to_encode):
	# your function


def decode(s_to_decode):
	# your function


class WordCountTests(unittest.TestCase):

    def test_encode(self):
        self.assertMultiLineEqual('2A3B4C', encode('AABBBCCCC'))

    def test_decode(self):
        self.assertMultiLineEqual('AABBBCCCC', decode('2A3B4C'))

    def test_encode_with_single(self):
        self.assertMultiLineEqual(
            '12WB12W3B24WB',
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    def test_decode_with_single(self):
        self.assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decode('12WB12W3B24WB'))

    def test_combination(self):
        self.assertMultiLineEqual('zzz ZZ  zZ', decode(encode('zzz ZZ  zZ')))

    def test_encode_unicode_s(self):
        self.assertMultiLineEqual('⏰3⚽2⭐⏰', encode('⏰⚽⚽⚽⭐⭐⏰'))

    def test_decode_unicode(self):
        self.assertMultiLineEqual('⏰⚽⚽⚽⭐⭐⏰', decode('⏰3⚽2⭐⏰'))
