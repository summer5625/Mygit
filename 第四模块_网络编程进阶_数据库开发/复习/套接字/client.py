# -*- coding: utf-8 -*-
# @Time    : 2019/7/20  13:54
# @Author  : XiaTian
# @File    : client.py
from socket import *

clint = socket(AF_INET, SOCK_STREAM)
clint.connect(('127.0.0.1', 8070))
while True:
    msg = input('>>:')
    if not msg: continue
    print('这厮:',msg)
    clint.send(msg.encode('utf-8'))
    print(1)
    data = clint.recv(1024)

    print(data.decode('utf-8'))