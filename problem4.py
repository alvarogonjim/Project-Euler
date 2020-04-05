#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Problem 4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from timer import timeit

__author__ = "Álvaro González Jiménez"
__license__ = "MIT"
__maintainer__ = "Álvaro González Jiménez"
__email__ = "alvarogonjim95@gmail.com"


@timeit
def largest_palindrome_product(digits):
    previous_palindrome = 0
    for i in range(10 ** (digits - 1), 10 ** (digits)):
        for j in range(10 ** (digits - 1), 10 ** (digits)):
            product = i * j
            if is_palindrome(product):
                if product > previous_palindrome:
                    previous_palindrome = product
    return previous_palindrome


def is_palindrome(number):
    number = str(number)
    reverse = number[::-1]
    return number == reverse


print(largest_palindrome_product(3))
