# -*- coding: utf-8 -*-
# @Time    : 2019/5/31  23:04
# @Author  : XiaTian
# @File    : 23、进程池线程池.py

# 进程池

# from concurrent.futures import ProcessPoolExecutor
# import os,time,random
#
# def task(name):
#     print('name:%s  pid:%s'%(name,os.getpid()))
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(5)  # 建立进程池，里面写参数代表进程池里面最大容纳进程数量，不写参数默认CPU最大核数
#                                    # 设置多少个进程从始至终就开启多少个进程，就有几个pid
#     start = time.time()
#     for i in range(5):
#         pool.submit(task,'process %s'%i).result()    # 向进程池里面放进程,异步提交任务即提交完任务后不用等任务运行，只是提交任务到进程池
#
#     pool.shutdown(wait=True)  # 关闭进程池入口，当提交完进程后计数器变为提交的进程个数，每执行完成一个任务，计数器减一，
#                               # 当计数器为0时执行该指令(有点像join)
#     stop = time.time()
#     print(stop - start)
#     print('主')


# 线程池

from concurrent.futures import ThreadPoolExecutor
from threading import currentThread
import os,random,time

def task():
    print('name:%s  pid:%s'%(currentThread().getName(),os.getpid()))
    time.sleep(2)


if __name__ == '__main__':

    pool = ThreadPoolExecutor(5)
    start = time.time()
    for i in range(5):
        pool.submit(task,)
    pool.shutdown()
    stop = time.time()
    print(stop - start)
    print('主')