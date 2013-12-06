#!/usr/bin/env python
# -*- coding: utf-8 -*-


def triplets(max_num):
    for x in range(1, max_num):
        y = x + 1
        z = y + 1
        if x % 50 == 0:
            print 'texting....', x
        while z <= max_num:
            while z ** 2 < x ** 2 + y ** 2:
                z = z + 1
            if x ** 2 + y ** 2 == z ** 2 and x + y + z == max_num:
                return x, y, z
            y = y + 1


print reduce(lambda x, y: x * y, triplets(1000))
