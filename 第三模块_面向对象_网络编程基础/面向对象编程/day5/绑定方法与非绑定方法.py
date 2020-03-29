# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 20:40
# @Author  : XiaTian
# @File    : 绑定方法与非绑定方法.py


'''
    一、绑定方法：绑定给谁就是谁调用，就会把把谁当做第一个参数传进去
        1、绑定到对象的方法：在类内部没有被装饰器装饰过的函数属性
        2、绑定到类的方法:在类内定义被classmethod装饰的方法
    二、非绑定方法：无法自动传值，之定义了一个普通函数，类和对象都可以调用
        不与类或者对象绑定，被staticmethod装饰的

    三、应用条件

'''

# classes Po:
#     print('hello')
#
# classes Foo:
#
#     def __init__(self,name):
#         self.name = name
#
#     def tell(self):
#         print('tell %s',self.name)
#
#     @classmethod
#     def func(cls,aa):
#         aa()
#         print(cls,aa)
#
#     @staticmethod
#     def func1(x,y):
#         print(x+y)
# f = Foo('夏天')
# Foo.func(Po)
# f.func(Po)

import hashlib
import time
import setting
class People:

    def __init__(self,name,sex,age):
        self.id = self.creat_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('name:%s  age:%s  sex:%s'%(self.name,self.age,self.sex))

    '需求：用户从配置文件里面读配置进行实例化'

    @classmethod
    def from_conf(cls):
        obj = cls(setting.name,setting.age,setting.sex)
        return obj

    '需求：需要给每个人编译个id'
    @staticmethod
    def creat_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

# 绑定给类的由类来调用，将类本身当做第一个参数传入
# p = People.from_conf()
# p.tell_info()
p1 = People('admin',18,'man')
p2 = People('yun',25,'man')
p3 = People('tian',28,'man')

print(p1.id)
print(p2.id)
print(p3.id)
print(p1.creat_id)
print(p1.tell_info)