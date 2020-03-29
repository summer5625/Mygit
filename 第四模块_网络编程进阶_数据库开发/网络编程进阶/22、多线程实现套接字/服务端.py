# -*- coding: utf-8 -*-
# @Time    : 2019/5/30  23:56
# @Author  : XiaTian
# @File    : 服务端.py

# from socket import *
# from threading import Thread
#
# def communicate(conn):
#
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data:break
#             conn.send(data.upper())
#         except ConnectionError:
#             break
#
#     conn.close()
#
#
# def clients(ip,port):
#     clients = socket(AF_INET,SOCK_STREAM)
#     clients.bind((ip,port))
#     clients.listen(5)
#
#     while True:
#         conn,addr = clients.accept()
#         t = Thread(target=communicate,args=(conn,))
#         t.start()
#
#     clients.close()
#
#
# if __name__ == '__main__':
#     clients('127.0.0.1',8070)



# 基于线程池实现

from socket import *
from concurrent.futures import ThreadPoolExecutor

def pp(conn):
    back = 'from pp'
    conn.send(back.encode('utf-8'))

def qq(conn):
    back = 'from qq'
    conn.send(back.encode('utf-8'))

def cc(conn):
    back = 'from cc'
    conn.send(back.encode('utf-8'))


def communicate(conn):

    while True:
        try:
            data = conn.recv(1024)
            number = data.decode('utf-8')
            if number == 1:
                pp(conn)
            elif number == 2:
                qq(conn)
            elif number == 3:
                cc(conn)
            else:
                continue
        except ConnectionError:
            break

    conn.close()


def clients(ip,port):
    clients = socket(AF_INET,SOCK_STREAM)
    clients.bind((ip,port))
    clients.listen(5)

    while True:
        conn,addr = clients.accept()
        pool.submit(communicate,conn)

    clients.close()


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    clients('127.0.0.1',8070)

# 基于gevent模块实现的并发

# from gevent import monkey,spawn;monkey.patch_all()
# from socket import *
#
#
# def communicate(conn):
#
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data:break
#             conn.send(data.upper())
#         except ConnectionError:
#             break
#
#     conn.close()
#
#
# def server(ip,port):
#     server = socket(AF_INET,SOCK_STREAM)
#     server.bind((ip,port))
#     server.listen(5)
#
#     while True:
#         conn,addr = server.accept()
#         spawn(communicate,conn)
#
#     server.close()


# if __name__ == '__main__':
#     g = spawn(server,'127.0.0.1',8070)
#     g.join()


