# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 20:45
# @Author  : XiaTian
# @File    : 继承与重用.py

# 继承：解决类与类之间重复代码问题，是一种创建新类的方式，新建的类可以继承一个或者多个父类


class Hero:
    # 定义每个英雄的名字，生命值，攻击力，防御
    def __init__(self, name, life_vale, aggressivity, physical_defense, magic_defense):
        self.name = name
        self.life_vale = life_vale
        self.aggressivity = aggressivity
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense


# 定义一个生产英雄的类
class ADC(Hero):

    # 定义英雄的技能和技能的伤害值
    def attack(self, enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.physical_defense) * 2


class AP(Hero):

    def skill(self, enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.magic_defense)


# 属性查找顺序

class Foo:
    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1()


class Bar(Foo):
    def f1(self):
        print('from Bar.f1')


print(Bar.__bases__)  # 查看继承的父类

b = Bar()

# b.f1()     # 从b本身的名称空间查找

b.f2()  # 由于b对象本身没有f2，开始从Bar类的名称空间查找f2，Bar类的名称空间也没有f2，则从其父类Foo名称空间查找f2
# 程序运行到f2()下面的self.f1()这句时此时这句可改写为b.f1(),运行到这行时即从b对象本身名称空间查找f1，而不是
# 运行Foo类名称空间中的f1


print(Bar.mro())  # 继承方法顺序
# 继承的实现原理
