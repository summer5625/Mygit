# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket
import struct
import json


download = r'D:\practice Python code\untitled\第三模块：面向对象&网络编程基础\网络编程\day4\客户端\download'
phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    cmd = input('>>:').strip()

    # 发命令
    phone.send(cmd.encode('utf-8'))

    # 1、接收服务端发来文件内容，以写的方式打开一个新文件
    obj = phone.recv(4)
    header_size = struct.unpack('i',obj)[0]

    # 2、收报头
    header_bytes = phone.recv(header_size)

    # 3、从报头解析真实数据信息
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    print(header_dict)
    file_size = header_dict['file_size']
    filename = header_dict['filename']

    # 4、接收真实数据
    with open(r'%s\%s'%(download,filename),'wb') as f:

        recv_size = 0
        while recv_size < file_size:  # 收数据，知道收完
            line = phone.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('总大小:%s    已下载大小:%s'%(file_size,recv_size))


phone.close()


