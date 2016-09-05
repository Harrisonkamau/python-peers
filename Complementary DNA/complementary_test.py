import unittest
from complementary import dna_strand


class complementary_test(unittest.TestCase):

    def test_single(self):
        self.assertEquals(dna_strand("AAAA"),"TTTT")

    def test_multiple(self):
        self.assertEquals(dna_strand("ATTGC"),"TAACG")

    def test_different(self):
        self.assertEquals(dna_strand("GTAT"),"CATA")
