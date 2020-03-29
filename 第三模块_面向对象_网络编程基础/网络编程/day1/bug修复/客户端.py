# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket

phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    c_msg = input('>>:').strip()
    if not c_msg:continue   # 加入判断输入是否为空，空则开始下一循环
    phone.send(c_msg.encode('utf-8'))
    print('end')
    data = phone.recv(1024)
    print(data.decode('utf-8'))
phone.close()


