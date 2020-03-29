# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 21:15
# @Author  : XiaTian
# @File    : 面向过程与面向对象.py
# @Software: PyCharm

# 面向过程：核心“过程”，实质是将需要实现的功能分成多个功能段，然后在按照特定的顺序去执行这些功能段，从而实现要求功能
# 优点：复杂问题流程化，将简单的问题简单化
# 缺点：可扩展性差，维护难度会高
# 用途：写一些简单的脚本程序

# 面向对象：
# 对象：所有独立存在的个体

# 定义一个类，定义类的关键字：classes
class LuffyStudents:
    school = '路飞学城'              # 类的数据属性

    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):                # 类的函数属性
        print('is learning')

    def eat(self):                  # 类的函数属性
        print('is eatting')

    def sleep(self):                # 类的函数属性
        print('is sleeping')

# print(LuffyStudents.__dict__)                     # 查看定义类后的名称空间
# print(LuffyStudents.__dict__['school'])           # 打印定义类后的名称空间
#
# # 查看类里面定义的属性
print(LuffyStudents.school)
print(LuffyStudents.eat)
print(LuffyStudents.learn)
print(LuffyStudents.sleep)
#
#
#
# # 向类里面增加属性
#
# LuffyStudents.country = 'China'
# print(LuffyStudents.__dict__)
#
# # 修改类里面的属性
#
# LuffyStudents.school = '罗高'
# print(LuffyStudents.school)
#
# # 删除类里面的属性
#
# del LuffyStudents.learn
# print(LuffyStudents.__dict__)

# stdu1 = LuffyStudents()
# print(stdu1)


# __init__方法后实例化步骤
# 1、先产生一个空对象
# 2、然后将产生的实例化对象，和对象的三个属性特征，共四个参数传给__init__

# stdu1 = LuffyStudents('李二','男',20)
# stdu2 = LuffyStudents('何芳华','女',23)

# 查看对象定制属性

# print(stdu1.__dict__)     # 查看名称空间
# print(stdu2.__dict__)

# print(stdu1.Name)
# print(stdu1.__dict__['Name'])

# 增加属性

# stdu2.Course = 'python全栈开发'
# print(stdu2.__dict__)

# 修改属性

# stdu1.Name = '夏天'
# print(stdu1.__dict__['Name'])


# 删除属性

# del stdu2.Course
# print(stdu2.__dict__)