#!/usr/bin/env python
# -*- coding: utf-8 -*-


from itertools import product


def palindrome(num):
    n = str(num)
    return n == n[::-1]


multiples = (
    (a, b) for a, b in product(xrange(100, 1000), repeat=2) if palindrome(a*b)
)

print max(multiples, key=lambda (a, b): a*b)
