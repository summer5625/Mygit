# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 11:47
# @Author  : XiaTian
# @File    : 属性查找.py
# @Software: PyCharm

# 定义一个类，定义类的关键字：classes

x = 'from global'

class LuffyStudents:
    school = '路飞学城'                # 类的数据属性

    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self,x):                # 类的函数属性
        print('%s is learning %s'%(self.Name,x))

    def eat(self,x):                  # 类的函数属性
        print('%s is eatting %s'%(self.Name,x))

    def sleep(self,x):                # 类的函数属性
        print('%s is sleeping %s'%(self.Name,x))

stu2 = LuffyStudents('刘三','女',24)
stu3 = LuffyStudents('夏天','男',26)

# print(LuffyStudents.school,id(LuffyStudents.school))
#类中的数据属性是所有对象共享的，在同一个内存地址取数据属性的数据
# print(stu2.school,id(stu2.school))
# print(stu3.school,id(stu3.school))

# 类的函数数据是绑定给对象用的，称为绑定到对象的方法。对象调用绑定方法时会把自己当做第一个参数传进函数

# print(LuffyStudents.learn)   # 类的函数属性中每个对象绑定的函数属性的内存地址是不同的
# print(stu2.learn)
# print(stu3.learn)

LuffyStudents.learn(stu2,'hard')
LuffyStudents.eat(stu2,'happy')
LuffyStudents.sleep(stu2,'well')

# stu2.eat('happy')
# stu3.sleep('good')


# 类中名称空间访问顺序



# 在stu2的名称空间内添加变量x
# stu2.x = 'from stu2'
# 在类的名称空间内添加变量x
# LuffyStudents.x = 'from LuffyStudents'

# 查看两个名称空间内的变量
# print(stu2.__dict__)
# print(LuffyStudents.__dict__)

# 类中名称空间访问顺序是先从对象本身名称空间查找，找不到就到类内部的名称空间查找，查找不到就到父类中查找，在查找不到就会报错，不会到全局名称空间查找
# print(stu2.x)


# python中一切皆对象
"""
    python中一切皆对象，在python3中统一了类和类型的概念
"""

