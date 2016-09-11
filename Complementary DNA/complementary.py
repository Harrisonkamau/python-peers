"""Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells 
and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA
; you need to get the other complementary side. DNA strand is never empty or there is no DNA at all.
"""


def dna_strand(DNA):
    list1 = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }

    complement = ""

    for i in DNA:
        if i in list1:
            complement += list1[i]
    return complement