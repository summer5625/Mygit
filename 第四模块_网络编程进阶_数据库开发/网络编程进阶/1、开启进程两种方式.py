# -*- coding: utf-8 -*-
# @Time    : 2019/5/20  23:28
# @Author  : XiaTian
# @File    : 1、开启进程两种方式.py

# 方式一：用process类来开启子进程

from multiprocessing import Process
import time,os

def task(name):

    print('%s is running'%name)
    time.sleep(3)
    print('%s is end'%name)

if __name__ == '__main__':

    # p = Process(target=task,kwargs={'name':'子进程1'})  # 字典形式传参
    p = Process(target=task,args=('子进程1',))
    p.start()  # 给操作系统发送开启进程的请求（此语句仅仅只是给操作系统发送一个信号）

    print('主')


# 方式二：自定义类来开启子进程
class MyProcess(Process):
    '''创建一个类来继承Process类'''

    def __init__(self,name):

        super().__init__()  # 重用继承父类的方法
        self.name = name

    def run(self):
        '''创建的方法名称必须叫run()'''
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is end' % self.name)


if __name__ == '__main__':
    p = MyProcess('子进程1')
    p.start()  # 调用的是自定义类中的run方法

    print('主')
