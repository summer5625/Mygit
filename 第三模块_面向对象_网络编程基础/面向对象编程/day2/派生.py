# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 21:34
# @Author  : XiaTian
# @File    : 派生.py

class Hero:
    # 定义每个英雄的名字，生命值，攻击力，防御
    def __init__(self, name, life_vale, aggressivity, physical_defense, magic_defense):
        self.name = name
        self.life_vale = life_vale
        self.aggressivity = aggressivity
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense

    def attack(self,enemy):            # 派生的函数属性
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1-enemy.physical_defense) * 2


# 定义一个生产英雄的类
class ADC(Hero):
    camp = 'high aggressivity'         # 派生的数据属性
    # 定义英雄的技能和技能的伤害值
    def attack(self,enemy):            # 派生的函数属性
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1-enemy.physical_defense) * 2
        print('from ADC attack')


class AP(Hero):
    camp = 'high skill aggressivity'
    # 定义英雄的技能和技能的伤害值
    def skill(self, enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.magic_defense)

# 当子类里面派生出与父类相同的属性，则以自己派生出的属性为主