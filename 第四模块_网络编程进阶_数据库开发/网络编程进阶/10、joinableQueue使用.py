# -*- coding: utf-8 -*-
# @Time    : 2019/5/26  23:03
# @Author  : XiaTian
# @File    : 10、joinableQueue使用.py

import time
from multiprocessing import Process,JoinableQueue

def producer(q,p):
    for i in range(2):
        res = '%s包子%s'%(p,i)
        time.sleep(2)
        print('%s生产了%s'%(p,res))

        q.put(res)
    q.join()

def consumer(q,c):
    while True:
        res = q.get()
        if res == None :break
        time.sleep(1)
        print('%s消费者吃了%s'%(c,res))
        q.task_done()  # 消费者给生产者发送结束信号

if __name__ == '__main__':

    q = JoinableQueue()
    q.join()

    #生产者
    p1 = Process(target=producer,args=(q,'p1'))
    p2 = Process(target=producer,args=(q,'p2'))


    # 消费者

    c1 = Process(target=consumer,args=(q,'c1'))
    c2 = Process(target=consumer,args=(q,'c2'))
    c1.daemon = True
    c2.daemon = True  # 将消费者进程守护起来确保生产者生产完后，消费者消费完后进程结束掉

    p1.start()
    p2.start()

    c1.start()
    c2.start()

    p1.join()   # 生产者生产完成后即结束进程
    p2.join()
    print('主')