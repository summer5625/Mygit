# -*- coding: utf-8 -*-
# @Time    : 2019/5/29  23:16
# @Author  : XiaTian
# @File    : 19、Event事件.py

# Event使用来实现线程与线程直接通讯的

# from threading import Thread,Event,currentThread
# import time
#
# event = Event()
#
# def student(name):
#     print('学生%s 正在听课'%name)
#     event.wait(1)   # 没有收到event.set()的信号程序就在此一直等待,当设置有数字时代表多少时间后超时自动确认
#     print('学生%s 课间活动'%name)
#
# def teacher(name):
#     print('%s老师 正在上课'%name)
#     time.sleep(5)
#     event.set()
#
#
# if __name__ == '__main__':
#     st1 = Thread(target=student,args=('alex',))
#     st2 = Thread(target=student,args=('egon',))
#     st3 = Thread(target=student,args=('wpq',))
#     t1 = Thread(target=teacher,args=('hsc',))
#
#     st1.start()
#     st2.start()
#     st3.start()
#     t1.start()

from threading import Thread,Event,currentThread,Condition
import time

event = Event()

# 建立连接
def conn():
    n = 0
    while not event.is_set(): # 检查event是否被设置
        if n == 3:
            print('%s try too many times'%currentThread().getName())
            return
        print('%s try %s'%(currentThread().getName(),n))
        event.wait(0.5)
        n += 1
    print('%s connected'%currentThread().getName())

# 检查是否连上服务器
def check():
    print('%s is checking'%currentThread().getName())
    time.sleep(1)
    event.set()


if __name__ == '__main__':  # 快捷方式输入main后按回车
    for i in range(3):
        t = Thread(target=conn)
        t.start()

    w = Thread(target=check)
    w.start()





