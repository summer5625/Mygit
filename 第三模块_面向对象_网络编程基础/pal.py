# -*- coding: utf-8 -*-
# @Time    : 2019/5/12  15:35
# @Author  : XiaTian
# @File    : pal.py

class People:

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def name(self):
        return self.__name

    @name.setter  # 函数添加修改类型的装饰器
    def name(self, val):
        print('setter', val)
        if not isinstance(val, str):
            print('名字必须是字符串')
            return
        self.__name = val

    @name.deleter  # 函数添加删除类型的装饰器
    def name(self):
        print('不允许删除')


people = People('夏天', 62, 1.68)
print(people.name)  # 查询操作
people.name = '田'  # 赋值操作
people.name = 123
del people.name  # 删除操作
print(people.name)
