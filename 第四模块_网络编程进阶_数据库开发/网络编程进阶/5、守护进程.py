# -*- coding: utf-8 -*-
# @Time    : 2019/5/24  23:43
# @Author  : XiaTian
# @File    : 5、守护进程.py

'''
    守护进程：守护进程会在主进程代码执行结束后就终止
            守护进程内无法再开启子进程,否则抛出异常
'''
from multiprocessing import Process
import time


def task(name):

    print('%s is running'%name)
    time.sleep(2)
    # pp = Process(target=time.sleep,args=(3,))
    # pp.start()   # 护进程内无法再开启子进程,否则抛出异常


if __name__ == '__main__':
    p = Process(target=task,args=('子进程',))

    p.daemon = True  # 设置守护进程，设置守护进程必须在子进程开启前，否则报错
    p.start()
    p.join()
    print('主')


def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")
