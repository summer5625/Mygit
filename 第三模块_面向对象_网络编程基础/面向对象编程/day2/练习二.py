# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 18:13
# @Author  : XiaTian
# @File    : 练习二.py

# 模仿王者荣耀定义两个英雄类
'''
要求：
    1、英雄需要有昵称，血量，技能，攻击力
    2、实例化两个英雄
    3、英雄之间可以互殴，被殴打一方掉血，血量等于0则判定死亡
'''

# 定义一个生产英雄的类
class ADC:

    # 定义每个英雄的名字，生命值，攻击力，防御
    def __init__(self, name, life_vale, aggressivity, physical_defense, magic_defense):
        self.name = name
        self.life_vale = life_vale
        self.aggressivity = aggressivity
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense

    # 定义英雄的技能和技能的伤害值
    def attack(self,enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1-enemy.physical_defense) * 2


class AP:

    def __init__(self, name, life_vale, aggressivity, physical_defense,magic_defense):
        self.name = name
        self.life_vale = life_vale
        self.aggressivity = aggressivity
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense

    def skill(self, enemy):
        enemy.life_vale = enemy.life_vale - self.aggressivity * (1 - enemy.magic_defense)


adc = ADC('寒冰射手',2000,350,0.4,0.5)
ap = AP('机械先驱',2000,600,0.5,0.3)

adc.attack(ap)
print(ap.life_vale)