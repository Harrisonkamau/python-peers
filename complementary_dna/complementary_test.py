import unittest
from complementary import dna_strand


class complementaryTest(unittest.TestCase):
    
    def test_same(self):
        self.assertEquals(dna_strand("AAAA"),"TTTT")
    
    def test_different(self):
        self.assertEquals(dna_strand("ATTGC"),"TAACG")
        
    def test_mixed(self):
        self.assertEquals(dna_strand("GTAT"),"CATA")
