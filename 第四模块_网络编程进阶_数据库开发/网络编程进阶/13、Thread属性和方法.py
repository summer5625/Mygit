# -*- coding: utf-8 -*-
# @Time    : 2019/5/27  0:40
# @Author  : XiaTian
# @File    : 13、Thread属性和方法.py

from threading import Thread,currentThread,active_count,enumerate
import time,os

def task():
    print('%s is running'%currentThread().getName()) # 获取线程名字
    time.sleep(1)
    print('%s in done'%currentThread().getName())

if __name__ == '__main__':

    t = Thread(target=task,name='线程1')
    t.start()
    # t.setName('儿子') #修改线程名字
    # currentThread().setName('主线程11')
    # t.join()
    # print(t.is_alive()) # 查看线程是否存活
    # print('主线程',currentThread().getName())
    # t.join()
    print(active_count()) # 查看运行线程数量
    print(enumerate())  # 取出活跃线程对象