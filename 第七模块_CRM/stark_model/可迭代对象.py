# -*- coding: utf-8 -*-
# @Time    : 2019/11/7  22:50
# @Author  : XiaTian
# @File    : 可迭代对象.py

# 如果一个类中定义了__iter__方法且该方法返回一个可迭代对象，那么就成该类的实例化对象时可迭代对象（可循环）
class SearchGroupRow(object):

    def __init__(self, queryset_or_tuple):
        self.data_list = queryset_or_tuple

    def __iter__(self):
        return iter([1, 2, 3])


row = SearchGroupRow([11, 22, 33])

for i in row:
    print(i)