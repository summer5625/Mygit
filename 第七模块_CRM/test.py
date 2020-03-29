# -*- coding: utf-8 -*-
# @Time    : 2019/12/26  14:52
# @Author  : XiaTian
# @File    : test.py
import socket


phone = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8070))
phone.listen(5)
conn,client_add = phone.accept()
data = conn.recv(1024)
conn.send(data.upper())
conn.close()
phone.close()



rec = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
phone.connect(('1270.0.0.1', 8070))
rec.send('hello'.encode('utf-8'))
da = rec.recv(1024)
rec.close()