# -*- coding: utf-8 -*-
# @Time    : 2019/5/25  0:17
# @Author  : XiaTian
# @File    : 6、互斥锁.py

from multiprocessing import Process,Lock
import time

def task(name,lock):
    lock.acquire()      # 上锁
    print('%s 1'%name)
    time.sleep(1)
    print('%s 2'%name)
    time.sleep(1)
    print('%s 3'%name)
    lock.release()

if __name__ == '__main__':
    lock = Lock()  # 给进程加锁
    for i in range(10):
        p = Process(target=task,args=('进程%s'%i,lock))
        p.start()