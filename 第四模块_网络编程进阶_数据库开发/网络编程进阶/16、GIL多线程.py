# -*- coding: utf-8 -*-
# @Time    : 2019/5/29  0:03
# @Author  : XiaTian
# @File    : 16、GIL多线程.py

# 计算密集型


# from multiprocessing import Process
# from threading import Thread
# import os,time
# # def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count()) #本机为12核
#     start=time.time()
#     for i in range(12):
#         p=Process(target=work) #耗时5s多
#         # p=Thread(target=work) #耗时18s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))
#



# I/O密集型
from multiprocessing import Process
from threading import Thread
import os,time
def work():
    time.sleep(2)
    print('===>')

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为12核
    start=time.time()
    for i in range(400):
        p=Process(target=work) #耗时8s多,大部分时间耗费在创建进程上
        # p=Thread(target=work) #耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))

# from threading import Thread,Lock
# import os,time
# def work():
#     global n
#     lock.acquire()
#     temp=n
#     time.sleep(0.1)
#     n=temp-1
#     lock.release()
# if __name__ == '__main__':
#     lock=Lock()
#     n=100
#     l=[]
#     for i in range(100):
#         p=Thread(target=work)
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#
#     print(n)