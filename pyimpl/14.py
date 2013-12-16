#!/usr/bin/env python
# -*- coding: utf-8 -*-


appeared_set = set()


def countChainLength(number):
    global appeared_set
    length = 1
    num = number
    appeared_set.add(num)
    while num > 1:
        appeared_set.add(num)
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        length += 1
    return length


max_length = 0
start_number = 0
for i in range(1000000, 100000, -1):
    if i in appeared_set:
        continue
    if i % 1000 == 0:
        print i, len(appeared_set)
    length = countChainLength(i)
    if length > max_length:
        max_length = length
        start_number = i

print max_length
print start_number
