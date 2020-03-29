# -*- coding: utf-8 -*-
# @Time    : 2019/6/16  11:03
# @Author  : XiaTian
# @File    : 服务.py

# from socket import *
# from threading import Thread,currentThread
# import queue


# class ThreadPool(Thread):
#
#     def __init__(self, sever, work_queue):
#         Thread.__init__(self)
#         self.sever = sever
#         self.work_queue = work_queue
#         self.add_thread = self.add_thread()
#
#     def add_thread(self):
#
#        while True:
#            self.conn, self.addr = self.sever.accept()
#            self.work_queue.put(self.conn)
#
#
# class Service(Thread):
#
#     def __init__(self, queue, sever):
#         Thread.__init__(self)
#         self.queue = queue
#         self.sever = sever
#         self.pool = ThreadPool(self.sever, self.queue)
#         self.pool.run()
#
#     def run(self):
#
#         while True:
#             try:
#
#                 connect = self.queue.get()
#                 print(connect)
#                 data = connect.recv(1024)
#                 print('接收:%s' % data.decode('utf-8'))
#                 if not data:break
#                 connect.send(data.upper())
#             except ConnectionError:
#                 break
#         connect.close()
#
#
# def main():
#
#     q = queue.Queue(5)
#     sever = socket(AF_INET,SOCK_STREAM)
#     sever.bind(('127.0.0.1', 8070))
#     sever.listen(5)
#     ser = Service(q, sever)
#     ser.run()
#
#
# main()


from socket import *
from threading import Thread, currentThread
import queue
import json
import struct


class ThreadPoolManger():
    """线程池管理器"""

    def __init__(self, thread_num):
        # 初始化参数
        self.work_queue = queue.Queue()
        self.thread_num = thread_num
        self.__init_threading_pool(self.thread_num)

    def __init_threading_pool(self, thread_num):
        # 初始化线程池，创建指定数量的线程池
        for i in range(thread_num):
            thread = ThreadManger(self.work_queue)
            thread.start()

    def add_job(self, func, *args):
        # 将任务放入队列，等待线程池阻塞读取，参数是被执行的函数和函数的参数
        self.work_queue.put((func, args))


class ThreadManger(Thread):
    """定义线程类，继承threading.Thread"""

    def __init__(self, work_queue):
        Thread.__init__(self)
        self.work_queue = work_queue
        self.daemon = True

    def run(self):
        # 启动线程
        while True:
            target, args = self.work_queue.get()
            target(*args)
            self.work_queue.task_done()


# 创建一个有4个线程的线程池
thread_pool = ThreadPoolManger(4)


def handle_request(conn_socket):

    while True:
        try:
            data = conn_socket.recv(4)
            head_size = struct.unpack('i', data)[0]
            msg_dict = conn_socket.recv(head_size)
            print('thread %s is running  recv:%s' %
                  (currentThread().getName(), msg_dict.decode('utf-8')))
            conn_socket.send(msg_dict.upper())
        except Exception:
            break
    # conn_socket.close()


socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('127.0.0.1', 8071))
socket.listen(5)


# 循环等待接收客户端请求
def run_forever():

    while True:
        # 阻塞等待请求
        conn_socket, addr = socket.accept()
        # 一旦有请求了，把socket扔到我们指定处理函数handle_request处理，等待线程池分配线程处理
        thread_pool.add_job(handle_request, *(conn_socket, ))
        print('thread %s is running' % currentThread().getName())

    socket.close()



run_forever()