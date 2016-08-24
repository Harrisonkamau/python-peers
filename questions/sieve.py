"""
Write a program that uses the Sieve of Eratosthenes to find all the primes from 2 up to a given number.

The Sieve of Eratosthenes is a simple, ancient algorithm for finding all
prime numbers up to any given limit. It does so by iteratively marking as
composite (i.e. not prime) the multiples of each prime,
starting with the multiples of 2.

Create your range, starting at two and continuing up to and including the given limit. (i.e. [2, limit])

The algorithm consists of repeating the following over and over:

- take the next available unmarked number in your list (it is prime)
- mark all the multiples of that number (they are not prime)

Repeat until you have processed each number in your range.

When the algorithm terminates, all the numbers in the list that have not
been marked are prime.

The wikipedia article has a useful graphic that explains the algorithm:
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Notice that this is a very specific algorithm, and the tests don't check
that you've implemented the algorithm, only that you've come up with the
correct list of primes.
"""

import unittest


def sieve(n):
	# your function


class SieveTest(unittest.TestCase):
    def test_a_few_primes(self):
        expected = [2, 3, 5, 7]
        self.assertEqual(expected, sieve(10))

    def test_prime_limit(self):
        expected = [2, 3, 5, 7]
        self.assertEqual(expected, sieve(7))

    def test_primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                    181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                    251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                    317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
                    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                    463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
                    557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
                    619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
                    787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
                    863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
                    953, 967, 971, 977, 983, 991, 997]
        self.assertEqual(expected, sieve(1000))

if __name__ == '__main__':
    unittest.main()
