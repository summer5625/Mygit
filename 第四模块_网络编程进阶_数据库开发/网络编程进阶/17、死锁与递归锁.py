# -*- coding: utf-8 -*-
# @Time    : 2019/5/29  22:38
# @Author  : XiaTian
# @File    : 17、死锁与递归锁.py

# 死锁
# from threading import Thread,Lock
# import time

# mutexA = Lock()
# mutexB = Lock()
#
# class MyThread(Thread):
#
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#
#         mutexA.acquire()
#         print('%s 拿到A锁'%self.name)
#
#         mutexB.acquire()
#         print('%s 拿到B锁'%self.name)
#
#         mutexB.release()
#         mutexA.release()
#
#     def f2(self):
#
#         mutexB.acquire()
#         print('%s 拿到B锁'%self.name)
#         time.sleep(0.1)
#
#         mutexA.acquire()
#         print('%s 拿到A锁'%self.name)
#
#         mutexA.release()
#         mutexB.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()


# 递归锁

from threading import Thread,RLock
import time

mutexB = mutexA = RLock()


class MyThread(Thread):

    def run(self):
        self.f1()
        self.f2()

    def f1(self):

        mutexA.acquire()
        print('%s 拿到A锁'%self.name)

        mutexB.acquire()
        print('%s 拿到B锁'%self.name)

        mutexB.release()
        mutexA.release()

    def f2(self):

        mutexB.acquire()
        print('%s 拿到B锁'%self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到A锁'%self.name)

        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()



