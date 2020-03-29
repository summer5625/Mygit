# -*- coding: utf-8 -*-
# @Time    : 2020/1/3  14:39
# @Author  : XiaTian
# @File    : 汉诺塔问题.py


def hanoi(n, a, b, c):

    if n > 0:
        hanoi(n-1, a, c ,b)
        print('moving from %s to %s' % (a, c))
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')