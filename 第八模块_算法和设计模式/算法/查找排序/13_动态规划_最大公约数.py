# -*- coding: utf-8 -*-
# @Time    : 2020/1/23  22:18
# @Author  : XiaTian
# @File    : 13_动态规划_最大公约数.py


# 最大公约数：
def gcb(a, b):

    if b == 0:
        return a
    else:
        return gcb(b, a % b)


# b = gcb(28, 21)
# print(b)


class Fraction:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcb(a, b)
        self.a /= x
        self.b /= x

    # 公约数
    def gcb(self, a, b):

        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    # 公倍数
    def zgs(self, a, b):
        x = self.gcb(a, b)
        return a * b / x

    # 求分数相加
    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        m = self.zgs(a, b)
        z = a * m / b + b * m / a
        return Fraction(z, m)

    # 将分数约分
    def __str__(self):
        return '%d/%d' % (self.a, self.b)


a = Fraction(30, 21)
b = Fraction(56, 81)
print(a+b)