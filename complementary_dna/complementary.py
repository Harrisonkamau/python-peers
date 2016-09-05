"""Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the 
"instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
You have function with one side of the DNA; you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all.
"""
strands ={"A":"T", "C":"G"}

def dna_strand(dna):
	if dna == "" or not isinstance(dna, str):
		raise ValueError("DNA strands can not be empty or non string")
	return "".join([strands.get(x) for x in dna.upper()])
