# -*- coding: utf-8 -*-
# @Time    : 2019/6/2  16:36
# @Author  : XiaTian
# @File    : 27、greenlet模块.py

from greenlet import greenlet
import time

def eat(name):

    print('%s eat1'%name)
    time.sleep(3)  # 遇到i\o不切
    p1.switch('egon')
    print('%s eat2'%name)
    p1.switch()

def play(name):

    print('%s play1'%name)
    g1.switch()
    print('%s play2'%name)


g1 = greenlet(eat)
p1 = greenlet(play)

g1.switch('egon')

