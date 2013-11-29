#!/usr/bin/env python
# -*- coding: utf-8 -*-


num = 100

sumSquare = sum([i**2 for i in range(1, num+1)])
squareSum = sum([i for i in range(1, num+1)])**2

print squareSum - sumSquare
