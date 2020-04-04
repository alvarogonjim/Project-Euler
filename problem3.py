#!/usr/bin/python

"""
Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from timer import timeit

__author__ = "Álvaro González Jiménez"
__license__ = "MIT"
__maintainer__ = "Álvaro González Jiménez"
__email__ = "alvarogonjim95@gmail.com"


@timeit
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


print largest_prime_factor(600851475143)
