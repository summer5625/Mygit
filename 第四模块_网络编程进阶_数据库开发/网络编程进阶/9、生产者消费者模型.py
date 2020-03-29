# -*- coding: utf-8 -*-
# @Time    : 2019/5/26  22:35
# @Author  : XiaTian
# @File    : 9、生产者消费者模型.py

import time
from multiprocessing import Process,Queue

def producer(q,p):
    for i in range(5):
        res = '%s包子%s'%(p,i)
        time.sleep(2)
        print('%s生产了%s'%(p,res))

        q.put(res)

def consumer(q,c):
    while True:
        res = q.get()
        if res == None :break  # 通过取数数据判断，容器内数据是否取完，取完则退出。不加此句则程序卡死
        time.sleep(1)
        print('%s消费者吃了%s'%(c,res))

if __name__ == '__main__':

    q = Queue()

    #生产者
    p1 = Process(target=producer,args=(q,'p1'))
    p2 = Process(target=producer,args=(q,'p2'))
    p3 = Process(target=producer,args=(q,'p3'))

    # 消费者

    c1 = Process(target=consumer,args=(q,'c1'))
    c2 = Process(target=consumer,args=(q,'c2'))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()


    p1.join()
    p2.join()
    p3.join()

    q.put(None) # 给消费者发送生产完成信号，此种方法有多少个消费者就需要发送多少个信号给消费者
    q.put(None)
    print('主')