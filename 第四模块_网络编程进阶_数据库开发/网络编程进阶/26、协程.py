# -*- coding: utf-8 -*-
# @Time    : 2019/6/2  0:02
# @Author  : XiaTian
# @File    : 26、协程.py

# 串行执行
import time

def consumer(res):
    print(len(res))

def producer():
    res = []
    for i in range(10000000):
        res.append(i)
    return res

start = time.time()
res = producer()
consumer(res)
stop = time.time()
print(stop-start)  # 1.266754150390625


#结果：10000
#     0.001088857650756836


# 基于yield实现并发：yield可以保存状态，send可以把一个函数的结果传递给另外一个函数

import time

def consumer():

    while True:
        x = yield
        # print(x)

def producer():
    res = consumer()
    next(res)
    for i in range(10000000):
        res.send(i)



start = time.time()
producer()
stop = time.time()
print(stop-start)  # 0.8062500953674316


# yield下遇到i\o操作

import time

def consumer():

    while True:
        x = yield
        # print(x)

def producer():
    res = consumer()
    next(res)
    for i in range(10):
        res.send(i)
        time.sleep(2)


start = time.time()
producer()
stop = time.time()
print(stop-start)  # 20.10326910018921