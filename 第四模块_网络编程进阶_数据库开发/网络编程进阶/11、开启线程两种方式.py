# -*- coding: utf-8 -*-
# @Time    : 2019/5/27  0:15
# @Author  : XiaTian
# @File    : 11、开启线程两种方式.py

#方式一
from threading import Thread
import time,os

'''
    在启动一个程序时即默认开启了一个线程，该程序中开启了两个线程
'''
# def task(name):
#
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is end'%name)
#
# if __name__ == '__main__':
#
#     # t = Thread(target=task,kwargs={'name':'子进程1'})  # 字典形式传参
#     t = Thread(target=task,args=('线程1',))
#     t.start()  # 给操作系统发送开启进程的请求（此语句仅仅只是给操作系统发送一个信号）
#
#     print('主线程')


# 方法二

class MyThread(Thread):
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
    t = MyThread('线进程1')
    t.start()  # 调用的是自定义类中的run方法

    print('主线程')
