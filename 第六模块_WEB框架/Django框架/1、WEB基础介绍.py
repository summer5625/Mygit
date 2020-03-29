# -*- coding: utf-8 -*-
# @Time    : 2019/9/24  11:38
# @Author  : XiaTian
# @File    : 1、WEB基础介绍.py

from socket import *

server = socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,addr = server.accept()
    data = conn.recv(1024)
    print(data)

    with open('login.html','r') as f:
        sendd = f.read()

    conn.send(('http/1.1 200 OK\r\n\r\n%s'%sendd).encode('utf8'))
    conn.close()
