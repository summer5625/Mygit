# -*- coding: utf-8 -*-
# @Time    : 2019/5/27  0:55
# @Author  : XiaTian
# @File    : 14、守护线程.py

from threading import Thread
import time

def task(name):
    time.sleep(2)
    print('%s say hello'%name)

if __name__ == '__main__':
    t1 = Thread(target=task,args=('xia',))
    t2 = Thread(target=task,args=('liu',))

    t1.daemon = True  # 守护线程，主线程结束后，守护线程立即结束
    t1.start()
    t2.start()

    print('主线程')
    print(t1.is_alive())

# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
#
# if __name__ == '__main__':
#     t1=Thread(target=foo)
#     t2=Thread(target=bar)
#
#     t1.daemon=True
#     t1.start()
#     t2.start()
#     print("main-------")
#
