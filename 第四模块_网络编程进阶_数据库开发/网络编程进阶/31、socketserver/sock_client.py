# -*- coding: utf-8 -*-
# @Time    : 2019/7/24
# @Author  : XiaTian
# @File    : sock_client.py

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8070))

while True:

    msg = input('>>:').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('接收:',data.decode('utf-8'))



client.close()