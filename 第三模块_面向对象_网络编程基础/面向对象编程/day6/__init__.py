# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 22:48
# @Author  : XiaTian
# @File    : __init__.py.py


a = {'a':1,'b':2,'c':3,'d':4}
for k,v in a.items():
    if k == 'c':
        a[k] = 8
print(a)

b = {'v':5}
a = b
print(a)