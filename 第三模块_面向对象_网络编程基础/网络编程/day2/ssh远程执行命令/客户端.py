# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket


phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    cmd = input('>>:').strip()

    # 发命令
    phone.send(cmd.encode('utf-8'))

    # 接服务端执行命令结果
    data = phone.recv(1024)
    print(data.decode('GB2312'))
phone.close()


