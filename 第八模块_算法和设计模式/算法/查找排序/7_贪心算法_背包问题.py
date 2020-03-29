# -*- coding: utf-8 -*-
# @Time    : 2020/1/16  17:05
# @Author  : XiaTian
# @File    : 7_贪心算法_背包问题.py
'''

固定容量的背包，去超市向背包里面放东西，使背包放的东西价值最多，物品可以散拿

'''
goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x: x[0]/x[1], reverse=True)


def fractional_backpack(goods, w):

    m = [0 for i in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if weight <= w:
            m[i] = 1
            total_v += prize
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return m


a = fractional_backpack(goods, 30)
print(a)