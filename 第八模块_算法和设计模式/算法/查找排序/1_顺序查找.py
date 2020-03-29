# -*- coding: utf-8 -*-
# @Time    : 2020/1/3  14:47
# @Author  : XiaTian
# @File    : 1_顺序查找.py
from cal_time import *


@cal_time
def liner_search(li , val):

    for index, v in enumerate(li):

        if v == val:
            return index
    else:
        return None


# 二分查找
@cal_time
def binary_search(li, val):

    left = 0
    right = len(li) - 1

    while left <= right:

        mid = (left + right) // 2

        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1

        elif li[mid] > val:
            right = mid - 1
    else:
        return None


li = list(range(100))
a = liner_search(li, 78)
b = binary_search(li, 78)

print(a, b)
