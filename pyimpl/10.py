#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


prime_set = set()


for num in xrange(2000000):
    if num % 10000 == 0:
        print 'testing...', num
    if isPrime(num):
        prime_set.add(num)


print sum(prime_set)
