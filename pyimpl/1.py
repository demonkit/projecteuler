#!/usr/bin/env python
# -*- coding: utf-8 -*-


def d(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    return False


if __name__ == '__main__':
    sum_ = 0
    for n in range(1, 1000):
        if d(n):
            sum_ += n
    print sum_
