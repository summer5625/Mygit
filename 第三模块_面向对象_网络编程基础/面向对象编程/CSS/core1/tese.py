# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 17:33
# @Author  : XiaTian
# @File    : tese.py

class B:

    def __str__(self):
        return 'str : class B'

    def __repr__(self):
        return 'repr : class B'


b = B()
print('%s' % b)
print('%r' % b)
