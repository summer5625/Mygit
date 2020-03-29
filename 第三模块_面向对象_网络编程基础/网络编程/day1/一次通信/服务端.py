# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 服务端.py

import socket

# 1、创建套接字（买手机）
phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# family表示套接字时基于什么通信的socket.AF_INET基于网络通信,AF_UNIX同一台机器通信;
# type是通信的类型SOCK_STREAM基于TCP协议，SOCK_DGRAM基于UDP协议
# print(phone)

# 2、绑定服务端IP地址和端口（绑定手机卡）
phone.bind(('127.0.0.1',8080))
# 127.0.0.1时本机回环地址用于本机测试，8080是绑定的端口，一台计算机有0-65535个端口，其中0-1024是给操作系统用的

# 3、开机
phone.listen(5)  # 5表示最大挂起连接数，即最多同时能有5台客户端能服务端通信

# 4、等待客户端请求访问（等电话链接）
print('start==>')
conn,client_addr = phone.accept()
# print('ok....')

# 5、收发消息
data = conn.recv(1024) # 1024代表收发消息的最大长度，单位：bytes
print('这是客户端的数据',data)

conn.send(data.upper())

# 6、挂电话
conn.close()

# 7、关机
phone.close()

'''
    服务端有两套套接字，一套为phone的套接字用于绑定服务端的IP和端口，监听，接收客户端连接；
    链接建立后会拿到conn这套套接字，用于收发消息
    
'''