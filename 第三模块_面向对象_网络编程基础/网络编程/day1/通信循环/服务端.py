# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 服务端.py

import socket


phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8081))
phone.listen(5)
print('start==>')
conn,client_addr = phone.accept()
print(client_addr)
while True:  # 通信循环
    data = conn.recv(1024)
    print('这是客户端的数据',data)
    conn.send(data.upper())
conn.close()
phone.close()
