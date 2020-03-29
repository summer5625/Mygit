# -*- coding: utf-8 -*-
# @Time    : 2019/6/4  22:05
# @Author  : XiaTian
# @File    : 客户端.py

from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8070))


while True:
    msg = input('>>:').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))


client.close()