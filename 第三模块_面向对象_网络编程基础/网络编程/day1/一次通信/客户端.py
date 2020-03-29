# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket

# 1、创建套接字（买手机）
phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 2、拨号
phone.connect(('127.0.0.1',8080))

# 3、发、收消息
a = {}
phone.send(str(a).encode('utf-8'))  # 网络通信传的的二进制，传消息时要先转换成二进制
data = phone.recv(1024)
print(data)

# 4、关闭
phone.close()


'''
    客户端只有一套套接字phone，用于发起建立链接请求，发收消息
'''