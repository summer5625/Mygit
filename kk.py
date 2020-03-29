# -*- coding: utf-8 -*-
# @Time    : 2020/2/6  14:46
# @Author  : XiaTian
# @File    : kk.py
import re

s = 'HG[3|B[2|CA]]F'
l = '[2|FGB[3|TYUH[3|DCD]]]'
b = s[:s.index(']')]
# print(b)
c = b.split('[')
e = c[-1].split('|')
# print(e)


def deco(s):

    if '[' not in s:
        return s

    a = s[:s.index(']')]
    b = a.split('[')
    c = b[-1].split('|')
    s_b = int(c[0]) * c[1]

    a_r = a[::-1]
    b_r = a_r[a_r.index('[')+1::]
    n_s = b_r[::-1] + s_b + s[s.index(']')+1::]
    return deco(n_s)


# rr = deco(s)
# print(rr)
# print('HGBCACABCACABCACAF')
# print(s[::-1])



class A:
    pass


# aa = A()
#
# print(id(aa))
# bb = A()
# print(id(bb))

class B(object):

    instant = None
    flag = True

    def __new__(cls, *args, **kwargs):

        if cls.instant is None:
            cls.instant = super().__new__(cls)
        return cls.instant

    def __init__(self, name):

        if not self.flag:
            return
        self.name = name
        B.flag = False


cc = B('summer')
print(id(cc))
print(cc.name)
dd = B('super')
print(id(dd))
print(dd.name)


















