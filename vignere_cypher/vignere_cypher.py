# coding=utf-8
"""The Vigenère Cipher is a polyalphabetic substitution cipher.
The 'key' for a vigenere cipher is a key word.

Read up on Vigenère Cipher before attempting solution: http://practicalcryptography.com/ciphers/classical-era/vigenere-gronsfeld-and-autokey/

Example: 'DEFENDTHEEASTWALLOFTHECASTLE' encyphered with the key 'FORTIFICATIONFORTIFICATIONFO'
should return 'ISWXVIBJEXIGGBOCEWKBJEVIGGQS'

Hint: If you've done caesar cipher before, you can use the same idea here
"""

from itertools import cycle
import string


def encode(key, plaintext):
    key = key.upper()
    plaintext = plaintext.upper()
    list1 = dict(zip(string.ascii_uppercase, range(26)))
    list2 = dict(zip(range(26), string.ascii_uppercase))
    result =''

    pairs = zip(cycle(key), plaintext)

    for i in range(len(pairs)):
        total = list1[pairs[i][0]] + list1[pairs[i][1]]
        result += list2[total % 26]

    return result
