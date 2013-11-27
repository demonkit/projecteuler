#!/usr/bin/env python
# -*- coding: utf-8 -*-


u2 = reset = 2
u3 = final = 600851475143
prime_list = []

largest = 1

while largest < u3:
    while u3 % u2:
        u2 += 1
    prime_list.append(u2)
    largest = u2
    u3 = u3 / u2
    u2 = reset

print largest, '================'
print prime_list
