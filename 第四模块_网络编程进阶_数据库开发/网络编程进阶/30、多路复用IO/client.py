# -*- coding: utf-8 -*-
# @Time    : 2019/6/4  23:27
# @Author  : XiaTian
# @File    : servers.py


from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8060))


while True:
    try:
        msg = input('>>:').strip()
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)

    except BlockingIOError:
        continue

client.close()