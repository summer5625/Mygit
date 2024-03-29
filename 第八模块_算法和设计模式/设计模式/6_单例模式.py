# -*- coding: utf-8 -*-
# @Time    : 2020/2/14  16:39
# @Author  : XiaTian
# @File    : 6_单例模式.py
from abc import abstractmethod, ABCMeta


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)

print(a.a)
print(b.a)
print(id(a), id(b))
