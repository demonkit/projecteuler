#!/usr/bin/env python
# -*- coding: utf-8 -*-


def findCheckList(largest):
    check_list = []
    for num in xrange(2, largest+1):
        for larger in xrange(largest, num, -1):
            if larger % num == 0:
                break
        else:
            check_list.append(num)
    return check_list


def findSolution(largest):
    check_list = findCheckList(largest)
    for num in xrange(largest, 99999999999999, largest):
        if all(num % n == 0 for n in check_list):
            return num
    return None


print findSolution(20)
