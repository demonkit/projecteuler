#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def countDivisors(num):
    nod = 0
    square = int(math.sqrt(num))
    for i in range(1, square+1):
        if num % i == 0:
            nod += 2
    if square ** 2 == num:
        nod -= 1
    return nod

i = 1
number = 0
while countDivisors(number) < 500:
    number += i
    i += 1

print number
