# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 22:27
# @Author  : XiaTian
# @File    : 在子类中重用父类的方法和属性.py

# 在子类中重用父类的方法和属性是为了减少重复代码，重用共有两种方法

# 方法一：指名道姓法（不依赖继承）
# classes Hero:
# #     # 定义每个英雄的名字，生命值，攻击力，防御
#     def __init__(self, name, life_vale, aggressivity, physical_defense, magic_defense):
#         self.name = name
#         self.life_vale = life_vale
#         self.aggressivity = aggressivity
#         self.physical_defense = physical_defense
#         self.magic_defense = magic_defense
# #
# # # 定义一个生产英雄的类
# classes ADC(Hero):
#     camp = 'high aggressivity'
#
#     def __init__(self,name, life_vale, aggressivity, physical_defense, magic_defense,weapon):
#         Hero.__init__(self,name, life_vale, aggressivity, physical_defense, magic_defense)   # 指明要调用父类的那些属性和方法
#         self.weapon = weapon
#
# #     # 定义英雄的技能和技能的伤害值
#     def attack(self,enemy):
#         enemy.life_vale = enemy.life_vale - self.aggressivity * (1-enemy.physical_defense) * 2
#
#
# classes AP(Hero):
#     camp = 'high skill aggressivity'
#
#     def __init__(self,name, life_vale, aggressivity, physical_defense, magic_defense,weapon):
#         Hero.__init__(self,name, life_vale, aggressivity, physical_defense, magic_defense) # 指明要调用父类的那些属性和方法
#         self.weapon = weapon
#
#     def skill(self, enemy):
#         enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.magic_defense)
#
# adc = ADC('艾希',2000,300,0.3,0.4,'arrow')
# ap = AP('维克托',2000,90,0.4,0.3,'truncheon')
#
# print(adc.__dict__)
# print(ap.__dict__)


# 方法二：在python2中supre(class_name,self)必须按照这种格式，在python3中可以简写为supre()，此种方法依赖继承

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
    camp = 'high aggressivity'

    def __init__(self, name, life_vale, aggressivity, physical_defense, magic_defense, weapon):
        super(ADC, self).__init__(name, life_vale, aggressivity, physical_defense, magic_defense)
        # 此种方法依赖继承，这句其本质上是类的属性绑定
        self.weapon = weapon

    # 定义英雄的技能和技能的伤害值
    def attack(self, enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.physical_defense) * 2


class AP(Hero):
    camp = 'high skill aggressivity'

    def __init__(self, name, life_vale, aggressivity, physical_defense, magic_defense, weapon):
        super().__init__(name, life_vale, aggressivity, physical_defense, magic_defense)
        self.weapon = weapon

    def skill(self, enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.magic_defense)


adc = ADC('艾希', 2000, 300, 0.3, 0.4, 'arrow')
ap = AP('维克托', 2000, 90, 0.4, 0.3, 'truncheon')


# print(adc.__dict__)
# print(ap.__dict__)

# super()继承原理

class A:

    def f1(self):
        print('from A')
        super().f3()


class B:

    def f2(self):
        print('from B')


class D:

    def f3(self):
        print('from D')
        # super().f2()


class C(A, B, D):
    pass


c = C()
print(C.mro())
c.f1()

# C的继承列表为：[<classes '__main__.C'>,
# <classes '__main__.A'>,
# <classes '__main__.B'>,
# <classes 'object'>]

# 打印结果：from A
# from B

# 由于c中没有f1就按照C中的mro列表顺序到A中查找f1，A中有f1则执行f1的函数，首先打印出来 ’from A‘
# 此时程序继续向下走开始执行super().f2()，由于super()具基于C的mro列表查找顺序继续向下查找的性质，开始到B中查找f2
