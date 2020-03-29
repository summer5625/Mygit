# -*- coding: utf-8 -*-
# @Time    : 2019/5/27  0:21
# @Author  : XiaTian
# @File    : 12、进程线程区别.py

# 开进程的开销远大于开线程

from multiprocessing import Process,current_process
from threading import Thread
import time,os

# def task(name):
#
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is end'%name)
#
# if __name__ == '__main__':
#
#     # p = Process(target=task,args=('子进程1',))
#     # p.start()
#     #
#     # print('主')
#
#     t = Thread(target=task, args=('线程1',))
#     t.start()
#
#     print('主线程')


# 同一进程内的多个线程共享该进程的地址空间

n = 100
def task():
    global n
    n = 0
    # print('子进程:%s  父进程:%s'%(os.getpid(),os.getppid()))
    print('线程:%s  父进程:%s'%(os.getpid(),os.getppid()))

if __name__ == '__main__':
    # p = Process(target=task,)
    # p.start()
    # p.join()
    #
    # print('主',current_process().pid)  # 主进程的内存空间和子进程内存空间是相互隔离的，在子进程中修改了全局变量，不会影响主进程的全局变量

    t = Thread(target=task,)
    t.start()
    t.join()
    print('主线程',os.getpid()) # 同一进程的多个线程共享内存空间

#