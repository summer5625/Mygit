# -*- coding: utf-8 -*-
# @Time    : 2020/1/3  15:23
# @Author  : XiaTian
# @File    : cal_time.py
import time


def cal_time(func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time: %s sec' % (func.__name__, t2 - t1))
        return result
    return wrapper