# -*- coding: utf-8 -*-
# @Time    : 2019/5/29  23:08
# @Author  : XiaTian
# @File    : 18、信号量.py

# 创造多把锁，让多个线程去抢

from threading import Thread,Semaphore,currentThread
import time,random

sm = Semaphore(value=3)  # 定义加锁的个数，3代表加了3把锁

def task():

    # sm.acquire()
    # print('%s in'%currentThread().getName())
    # time.sleep(random.randint(1,3))
    # sm.release()

    # 简写方法
    with sm:
        print('%s in' % currentThread().getName())
        time.sleep(random.randint(1, 3))



if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task,)
        t.start()

