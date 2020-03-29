# -*- coding: utf-8 -*-
# @Time    : 2020/1/7  15:41
# @Author  : XiaTian
# @File    : print_model.py

def fun(li, n, st=''):

    mid = (li[0] + li[-1]) // 2
    if len(st) >= 6:
        return st

    if n < mid:
        st += '0'
        return fun([li[0], mid], n, st)
    elif n > mid:
        st += '1'
        return fun([mid, li[-1]], n, st)
    else:
        st += '1'
        return st


a = fun([-90, 90], 45)
print(a)


def Fibonacci(max):

    n, a, b = 0, 0, 1

    while n < max:
        # print(b)
        a, b = b, a+b
        n += 1
    return b


def f(n, count=0):

    if n == 0:
        return count
    if n % 2 == 1:
        count += 1
        return f(n-1, count)
    else:
        count += 1
        return f(n-2, count)




















