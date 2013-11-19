#!/usr/bin/env python
# -*- coding: utf-8 -*-


def even(num):
    return num % 2 == 0


def nextFib(num1, num2):
    num3 = num1 + num2
    return (num2, num3)


if __name__ == '__main__':
    biggest = 4000000
    first = 1
    second = 2
    third = first + second
    sum_ = second
    while third <= biggest:
        if even(third):
            sum_ += third
        first, second = nextFib(first, second)
        third = first + second
    print sum_
