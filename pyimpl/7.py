#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


DEBUG = False
counter = 10001
prime_cnt = 0
cur_prime = None
number = 1


def isPrime(num):
    if num in (1, 4):
        return False
    if num in (2, 3):
        return True
    for i in xrange(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True


if len(sys.argv) > 1 and sys.argv[1] == 'd':
    DEBUG = True
    counter = 6
    import pdb
    pdb.set_trace()


while prime_cnt < counter:
    number += 1
    if isPrime(number):
        cur_prime = number
        prime_cnt += 1
    if number / 100000:
        print number, prime_cnt
    if DEBUG:
        print number, prime_cnt


print
print
print cur_prime
