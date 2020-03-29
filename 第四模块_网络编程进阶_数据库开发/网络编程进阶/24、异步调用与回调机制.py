# -*- coding: utf-8 -*-
# @Time    : 2019/5/31  23:54
# @Author  : XiaTian
# @File    : 24、异步调用与回调机制.py


'''
提交任务的两种方式：
    1、同步调用：提交完任务后，就在原地等待任务执行完毕，拿到结果，在执行下一行代码；导致程序串行执行
    2、异步调用:提交任务后

'''

# 同步调用

from concurrent.futures import  ThreadPoolExecutor
import time,random

def la(name):
    print('%s is laing'%name)
    time.sleep(random.randint(3,6))
    res = random.randint(6,10)*'#'

    return {'name':name,'res':res}

def weight(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 啦了 %sKg'%(name,size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)

    shit1 = pool.submit(la,'alex').result()
    weight(shit1)

    shit2 = pool.submit(la,'engon').result()
    weight(shit2)

    shit3 = pool.submit(la,'wpq').result()
    weight(shit3)


# 异步调用

from concurrent.futures import  ThreadPoolExecutor
import time,random

def la(name):
    print('%s is laing'%name)
    time.sleep(random.randint(3,6))
    res = random.randint(6,10)*'#'

    weight({'name':name,'res':res})

def weight(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 啦了 %sKg'%(name,size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)

    pool.submit(la,'alex')
    pool.submit(la,'engon')
    pool.submit(la,'wpq')


# 异步调用+回调函数
import time,random
from concurrent.futures import  ThreadPoolExecutor


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3,6))
    res = random.randint(6,10)*'#'

    return {'name': name,'res': res}


def weight(shit):
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 啦了 %sKg'%(name,size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    pool.submit(la,'alex').add_done_callback(weight)
    pool.submit(la,'engon').add_done_callback(weight)
    pool.submit(la,'wpq').add_done_callback(weight)

















