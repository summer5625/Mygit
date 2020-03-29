# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket


phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    c_msg = input('>>:').strip()
    phone.send(str(c_msg).encode('utf-8'))
    data = phone.recv(1024)
    print(data)
phone.close()


