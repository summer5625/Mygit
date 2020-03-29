# -*- coding: utf-8 -*-
# @Time    : 2019/7/29  18:49
# @Author  : XiaTian
# @File    : 习题编程.py



"""
1、请写一个包含10个线程的程序，主线程必须等待每一个子线程执行完成之后才结束执行，每一个子线程执行的时候都需要打印当前线程名、
   当前活跃线程数量以及当前线程名称；

"""
from threading import Thread, currentThread, active_count, Semaphore, Timer
from concurrent.futures import ThreadPoolExecutor
import queue
import time


def task():

    print('正在运行:%s  alive_count:%s' % (currentThread().getName(), active_count()))
    time.sleep(1)


# if __name__ == '__main__':
#
#     for i in range(10):
#         t = Thread(target=task)
#         t.start()
#         t.join()
#
#     print('over')

"""
2、请写一个包含10个线程的程序，并给每一个子线程都创建名为"name"的线程私有变量，变量值为“Alex”；
"""

def task1():
    name = 'Alex'
    print('正在运行:%s  alive_count:%s' % (currentThread().getName(), active_count()))
    time.sleep(1)


# if __name__ == '__main__':
#
#     for i in range(10):
#         t = Thread(target=task1)
#         t.start()
#         t.join()
#
#     print('over')


"""
3、请使用协程写一个消费者生产者模型；
"""


# def consumer():
#     while True:
#         x = yield
#         print(x)
#
#
# def producer():
#
#     res = consumer()
#     next(res)
#     for i in range(10):
#         res.send(i)
#
# producer()

"""
4、写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；
"""


def delayed(past):
    time.sleep(1)
    print('past:%s now:%s' % (past, time.time()))


# if __name__ == '__main__':
#
#     date = time.time()
#     time.sleep(10)
#     for i in range(10):
#         t = Thread(target=delayed, args=(date,))
#
#         t.start()


"""
5、写一个程序，包含十个线程，同时只能有五个子线程并行执行；
"""


def parallel():

    print('%s' % currentThread().getName())
    time.sleep(2)



# if __name__ == '__main__':
#
#     poll = ThreadPoolExecutor(5)
#     for i in range(10):
#         poll.submit(parallel,)
#
#     poll.shutdown()


"""
6、写一个程序 ，包含一个名为hello的函数，函数的功能是打印字符串“Hello, World!”，该函数必须在程序执行30秒之后才开始执行
(不能使用time.sleep())；

"""


def hello():
    print('Hello, World!')
    print(time.time())


# if __name__ == '__main__':
#     t = Timer(30,hello)
#     print(time.time())
#     t.start()


"""
7、写一个程序，利用queue实现进程间通信；
"""

from multiprocessing import Process, Queue,Pipe

# def producer(q, name):
#     for i in range(6):
#         res = '%s %s '% (name, i)
#         time.sleep(1)
#         q.put(res)
#
# def consumer(q):
#     while True:
#         data = q.get()
#         time.sleep(3)
#         if data == None: break
#         print(data)

# if __name__ == '__main__':
#     q = Queue(5)
#     p = Process(target=producer, args=(q, 'p1'))
#     c = Process(target=consumer, args=(q,))
#
#     p.start()
#     c.start()
#
#     p.join()
#
#
#     q.put(None)


"""
8、写一个程序，利用pipe实现进程间通信；
"""


# def consumer(p, name):
#     left, right = p
#     left.close()
#     while True:
#         try:
#             baozi = right.recv()
#             print('%s 收到包子:%s' % (name, baozi))
#         except EOFError:
#             right.close()
#             break
#
#
# def producer(seq,p):
#     left, right = p
#     right.close()
#     for i in seq:
#         left.send(i)
#     else:
#         left.close()
#
#
# if __name__ == '__main__':
#     left, right = Pipe()
#
#     c1 = Process(target=consumer, args=((left, right), 'c1'))
#     c1.start()
#
#     seq = (i for i in range(5))
#     producer(seq, (left, right))
#
#     right.close()
#     left.close()
#
#     c1.join()
#     print('主进程')


"""
9、使用selectors模块创建一个处理客户端消息的服务器程序；
"""
# from socket import *
# import selectors
#
# sel = selectors.DefaultSelector()
#
# def accpet(server):
#     conn, addr = server.accept()
#     sel.register(conn, selectors.EVENT_READ, task)
#
#
# def task(conn):
#     try:
#         data = conn.recv(1024)
#         if not data:
#             print('closing', conn)
#             sel.unregister(conn)
#             conn.close()
#             return
#         conn.send(data.upper())
#     except Exception:
#         print('closing', conn)
#         sel.unregister(conn)
#         conn.close()
#
#
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('127.0.0.1', 8070))
# server.listen(5)
# server.setblocking(False)
# sel.register(server, selectors.EVENT_READ, accpet)
#
# while True:
#     events = sel.select()
#     for sel_obj, mask in events:
#         callback = sel_obj.data
#         print(mask)
#         callback(sel_obj.fileobj)


"""
10、使用socketserver创建服务器程序时，如果使用fork或者线程服务器，一个潜在的问题是，恶意的程序可能会发送大量的请求导致服务器崩溃，
请写一个程序，避免此类问题；
"""

import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        pool = ThreadPoolExecutor(10)
        while True:
            pool.submit(self.task,)
        pool.shutdown()

    def task(self):
        while True:

            data = self.request.recv(1024)
            print('hhh:',data)
            if not data:continue
            print('接收:%s' % data.decode('utf-8'))
            self.request.send(data.upper())
            break


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8070), MyServer)
server.serve_forever()





















