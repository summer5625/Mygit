# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 20:49
# @Author  : XiaTian
# @File    : 练习1.py

'''
需求：
    在元类中控制把自定义类的数据属性都变成大写
分析：
    通过自定义元类来控制创建类的行为
    1、类中数据属性的特点:前面没有‘__',不能 .() 调用
'''

# classes Foo:
#     country = 'China'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def tt(self):
#         print('tt')
#
# print(Foo.__dict__)

class Mymeta(type):

    def __init__(self,class_name,class_bases,class_dict):
        new_dict = {}
        for k,v in class_dict.items():
            if not k.startswith('__') and str(class_dict[k]) == v:
                new_dict[k.upper()] = v
            else:
                new_dict[k] = v
        super(Mymeta,self).__init__(class_name,class_bases,class_dict)

class Chinese(object,metaclass = Mymeta):

    country = 'China'
    camp = 'read'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking'% self.name)

print(Chinese.__dict__)