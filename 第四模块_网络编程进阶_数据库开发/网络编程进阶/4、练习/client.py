# -*- coding: utf-8 -*-
# @Time    : 2019/5/24  23:05
# @Author  : XiaTian
# @File    : servers.py

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))
while True:
    msg = input('>>:').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))