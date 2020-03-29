# -*- coding: utf-8 -*-
# @Time    : 2019/6/2  17:12
# @Author  : XiaTian
# @File    : 28、gevent模块.py


# 检测gevent模块自己的i\o
# import gevent
# import time
#
#
#
# def eat(name):
#
#     print('%s eat1'%name)
#     time.sleep(2)#gevent.sleep(2)
#     print('%s eat2'%name)
#
#
# def play(name):
#
#     print('%s play1'%name)
#     time.sleep(5) #gevent.sleep(5)  # gevent模块下检测得i\o操作，只能检测到gevent模块自己的i\o，要想检测所有i\o需要导入其他功能模块
#     print('%s play2'%name)
#
#
# # 提交任务异步提交
# start = time.time()
# g1 = gevent.spawn(eat,'egon')
# g2 = gevent.spawn(play,'egon')
#
# g1.join()
# g2.join()
# stop = time.time()
# print(stop-start)


# 检测所有i\o
# from gevent import monkey
# monkey.patch_all()  # 设置检测所有i\o
# import gevent
# import time
#
#
#
# def eat(name):
#
#     print('%s eat1'%name)
#     time.sleep(2)#gevent.sleep(2)
#     print('%s eat2'%name)
#
#
# def play(name):
#
#     print('%s play1'%name)
#     time.sleep(5) #gevent.sleep(5)
#     print('%s play2'%name)
#
#
# # 提交任务异步提交
# start = time.time()
# g1 = gevent.spawn(eat,'egon')
# g2 = gevent.spawn(play,'egon')
#
# g1.join()
# g2.join()
# gevent.joinall([g1,g2]) # 元组或者列表
# stop = time.time()
# print(stop-start)

from gevent import monkey
monkey.patch_all()  # 设置检测所有i\o


import time
import gevent
from threading import currentThread




def eat(name):

    print('%s eat1 %s' % (name, currentThread().getName()))
    time.sleep(2)  # gevent.sleep(2)
    print('%s eat2' % name)


def play(name):

    print('%s play1 %s' % (name, currentThread().getName()))
    time.sleep(5)  # gevent.sleep(5)
    print('%s play2' % name)


# 提交任务异步提交
start = time.time()
g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, 'egon')

time.sleep(6)
stop = time.time()
print(stop - start)
