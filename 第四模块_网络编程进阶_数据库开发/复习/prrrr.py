# -*- coding: utf-8 -*-
# @Time    : 2019/7/20  14:40
# @Author  : XiaTian
# @File    : prrrr.py
from multiprocessing import Process,Queue
import time
import selectors


def producer(name, q):
    print('%s 正在生产' % name)
    res = '生产1'
    time.sleep(2)
    q.put(res)

    print('%s 生产完成' % name)


def consumer(name, q):
    while True:
        data = q.get()
        if not data:break
        print('%s 正在消费 %s' % (name,data))
        time.sleep(2)
        print('%s 消费完成' % name)


# if __name__ == '__main__':
#
#     q = Queue(3)
#     p1 = Process(target=producer, args=('生产1',q))
#     p2 = Process(target=producer, args=('生产2',q))
#
#     c1 = Process(target=consumer, args=('消费1',q))
#     c2 = Process(target=consumer, args=('消费1',q))
#
#     p1.start()
#     p2.start()
#
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)

print(int('10001001',2))


se = selectors.DefaultSelector()
