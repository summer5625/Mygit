# -*- coding: utf-8 -*-
# @Time    : 2020/1/16  17:01
# @Author  : XiaTian
# @File    : 6_贪心算法_找零问题.py

t = [100, 50, 20, 10, 5, 1]


def change(t, n):

    m = [0 for i in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money

    return m, n


a = change(t, 376)
print(a)