# -*- coding: utf-8 -*-
# @Time    : 2019/6/20
# @Author  : XiaTian
# @File    : sock_server.py


import socketserver

class MyServer(socketserver.BaseRequestHandler):  # 定义套接字类，类必须继承socketserver.BaseRequestHandler类

    def handle(self): # 必须定义函数名为handle的函数属性，里面放需要并发的代码
        while True:
            data = self.request.recv(1024)
            if not data:continue
            print('接收:',data.decode('utf-8'))
            while True:
                res = input('>>:').strip()
                if not res:continue
                self.request.send(res.encode('utf-8'))
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1', 8070), MyServer) # 第二部固定格式
server.serve_forever()  # 固定格式不变
