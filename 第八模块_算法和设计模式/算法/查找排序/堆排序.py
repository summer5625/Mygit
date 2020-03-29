# -*- coding: utf-8 -*-
# @Time    : 2020/2/10  13:20
# @Author  : XiaTian
# @File    : 堆排序.py
import re


s = '[11, 2, 3, 4, 5]'

a = re.findall('(?P<item>\d+)', s)
print(a)