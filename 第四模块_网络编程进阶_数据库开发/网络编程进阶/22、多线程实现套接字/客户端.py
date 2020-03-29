# -*- coding: utf-8 -*-
# @Time    : 2019/5/30  23:56
# @Author  : XiaTian
# @File    : 客户端.py
from socket import *
from threading import Thread,currentThread


def clients():
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.1',8070))

    while True:
        msg = input('>>:').strip()
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))

    client.close()


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=clients)
        t.start()



