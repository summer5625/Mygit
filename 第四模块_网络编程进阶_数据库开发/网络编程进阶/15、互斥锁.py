# -*- coding: utf-8 -*-
# @Time    : 2019/5/27  1:27
# @Author  : XiaTian
# @File    : 15、互斥锁.py

from threading import Thread,Lock,currentThread
import time

# 不加锁
# n = 100
# def task():
#     global n
#     temp = n
#     time.sleep(0.1)
#     n = temp - 1
#
# '''
#     开启100个线程，共享同一个内存空间，在程序开启后每个线程也开启，同时获取到n=100，然后程序暂停0.1秒
#     然后每个线程开始执行下面代码，所以结果为99
# '''
# if __name__ == '__main__':
#     t_l = []
#     for i in range(100):
#         t = Thread(target=task,)
#         t_l.append(t)
#         t.start()
#
#     for t in t_l:
#         t.join()
#
#     print('主',n)



# 加锁

n = 100
def task(i):
    global n
    mutex.acquire()
    print('%s 线程%s' % (currentThread().getName(), i))
    temp = n
    time.sleep(0.1)
    n = temp - 1
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target=task,args=(i,))
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    print('主',n)