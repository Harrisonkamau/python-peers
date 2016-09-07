import unittest
from vignere_cypher import encode


class cypherTest(unittest.TestCase):

    def test_easy(self):
        self.assertEqual('ISWXVIBJEXIGGBOCEWKBJEVIGGQS', encode('FORTIFICATIONFORTIFICATIONFO', 'DEFENDTHEEASTWALLOFTHECASTLE'))

    def test_short_key(self):
        self.assertEqual('HFNLPYOSND', encode('ABC', 'HELLOWORLD'))

    def test_capitalistion(self):
        self.assertEqual('ECUVGKOXKWWURKX', encode('secretkey', 'mysecretmessage'))

if __name__ == '__main__':
    unittest.main()
