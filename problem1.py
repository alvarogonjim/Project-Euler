#!/usr/bin/python

"""
Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from timer import timeit

__author__ = "Álvaro González Jiménez"
__license__ = "MIT"
__maintainer__ = "Álvaro González Jiménez"
__email__ = "alvarogonjim95@gmail.com"


@timeit
def multiplies_3_5(number):
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result = result + i
    return result


print(multiplies_3_5(1000))
