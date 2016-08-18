# -*- coding: utf-8 -*-
"""
Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.

The Atbash cipher is a simple substitution cipher that relies on
transposing all the letters in the alphabet such that the resulting
alphabet is backwards. The first letter is replaced with the last
letter, the second with the second-last, and so on.

An Atbash cipher for the Latin alphabet would be as follows:

```plain
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba
```

It is a very weak cipher because it only has one possible key, and it is
a simple monoalphabetic substitution cipher. However, this may not have
been an issue in the cipher's time.

Ciphertext is written out in groups of fixed length, the traditional group size
being 5 letters, and punctuation is excluded. This is to make it harder to guess
things based on word boundaries.

## Examples
- Encoding `test` gives `gvhg`
- Decoding `gvhg` gives `test`
- Decoding `gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt` gives `The quick brown fox jumps over the lazy dog.`

"""
import unittest


# your functions
def decode(cipher):
	
def encode(plain):
	

class AtbashCipherTest(unittest.TestCase):

    def test_encode_no(self):
        self.assertMultiLineEqual("ml", encode("no"))

    def test_encode_yes(self):
        self.assertMultiLineEqual("bvh", encode("yes"))

    def test_encode_OMG(self):
        self.assertMultiLineEqual("lnt", encode("OMG"))

    def test_encode_O_M_G(self):
        self.assertMultiLineEqual("lnt", encode("O M G"))

    def test_encode_long_word(self):
        self.assertMultiLineEqual("nrmwy oldrm tob", encode("mindblowingly"))

    def test_encode_numbers(self):
        self.assertMultiLineEqual("gvhgr mt123 gvhgr mt",
                                  encode("Testing, 1 2 3, testing."))

    def test_encode_sentence(self):
        self.assertMultiLineEqual("gifgs rhurx grlm",
                                  encode("Truth is fiction."))

    def test_encode_all_things(self):
        plaintext = "The quick brown fox jumps over the lazy dog."
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        self.assertMultiLineEqual(ciphertext, encode(plaintext))

    def test_decode_word(self):
        self.assertMultiLineEqual("exercism", decode("vcvix rhn"))

    def test_decode_sentence(self):
        self.assertMultiLineEqual(
            "anobstacleisoftenasteppingstone",
            decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v")
        )


if __name__ == '__main__':
    unittest.main()
