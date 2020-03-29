# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 服务端.py

import socket


phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 当IP和端口已经存在时重用存在的ip和端口，因为当启用一个服务端然后关闭后操作系统未及时回收端口

phone.bind(('127.0.0.1',8081))
phone.listen(5)
print('start==>')
while True:   # 加链接上循环保证服务端能一直对外提供服务，但一次只能服务一个对象，服务完一个对象才能对下一个对象提供服务
    conn,client_addr = phone.accept()
    print(client_addr)
    while True:  # 通信循环
        try:                           # windows下加入try方法
            data = conn.recv(1024)
            if not data:break          # linux系统下加入非空判断，客户端关闭时，服务端也关闭
            print('这是客户端的数据',data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()
phone.close()


