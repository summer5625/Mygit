# -*- coding: utf-8 -*-
# @Time    : 2020/1/16  22:11
# @Author  : XiaTian
# @File    : 8_贪心算法_数字拼接.py
'''

有n个非负整数，将其安按照字符串拼接方式拼接为一个整数，如何拼接可以等得到最大的整数

'''
from functools import cmp_to_key


li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return ''.join(li)


c = number_join(li)
print(c)
# a = list(map(str, li))
# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         print(i, '--', j)

