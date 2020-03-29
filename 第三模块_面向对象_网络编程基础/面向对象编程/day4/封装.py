# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 22:10
# @Author  : XiaTian
# @File    : 封装.py


# 隐藏属性

# classes A:
#
#     __a = 3                    # 在定义阶段就将__a变形为_A__a
#
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#
#     def info(self):
#         print('My name is %s,i am %s'%(self.name,self.__age))        # 在类内部可以访问隐藏属性
#
#
# a = A('aa',25)
#
# # print(a.__age)                  # 在类外部无法访问隐藏属性，会报错
# a.info()
#
# A.__sex = '女'                    # 在类外部无法定义隐藏的属性
#
# print(A.__dict__)
# print(a.__sex)
#
#
# classes FOO:
#
#     def __func(self):                # 定义时即改写为_Foo__func()
#         print('from Foo')
#
#     def bar(self):
#         print('from bar')
#         self.__func()               # 此时调用的__func()不是子类里面的，是父类的即_Foo__func()
#
# classes Bar(FOO):
#
#     def __func(self):               # 定义时即改写为_Bar__func
#         print('from Bar')
#
# b = Bar()
# b.bar()


# 封装数据属性：明确的区分内外,控制外部对隐藏属性的操作

class People:

    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def info(self):
        print('name:<%s> age:<%s> sex:<%s>'%(self.__name,self.__age,self.__sex))

    def change_info(self,name,age,sex):
        if not isinstance(name, str):
            print('名字必须是字符串')
            return

        if not isinstance(age, int):
            print('名字必须是字符串')
            return

        if not isinstance(name, str):
            print('性别必须是字符串')
            return

        self.__name = name
        self.__age = age
        self.__sex = sex

p = People('刘三',25,'女')

p.info()
p.change_info(24,'na','meal')


# 封装方法属性：隔离复杂度，同时也提升了安全性
# 将实现魔衣功能的诸多功能块，通过隐藏属性隐藏起来，然后开放一个接口将这些功能块打包起来统一调用

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()
a.withdraw()


# 封装扩展性

# 初始程序
class Room:

    def __init__(self,name,owner,weight,length,height):
        self.name = name
        self.owner =owner
        self.__weight = weight
        self.__length = length
        self.__height = height

    def area(self):

        s = self.__weight * self.__length


        return s

room = Room('刘三','别墅',20,20,15)

# 扩展功能：即永恒调用时只会调用接口的名称，只要接口名称不变，改变接口内部的代码既可以实现不同的功能

class Room:

    def __init__(self,name,owner,weight,length,height):
        self.name = name
        self.owner =owner
        self.__weight = weight
        self.__length = length
        self.__height = height

    def area(self):


        v = self.__weight * self.__length * self.__height  # 计算方式发生变化

        return v

room = Room('刘三','别墅',20,20,15)