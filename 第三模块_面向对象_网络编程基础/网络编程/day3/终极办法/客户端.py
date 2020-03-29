# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket
import struct


phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    cmd = input('>>:').strip()

    # 发命令
    phone.send(cmd.encode('utf-8'))

    # 1、先拿固定长度报头
    obj = phone.recv(4)

    # 2、从报头解析真实数据信息
    total_size = struct.unpack('i', obj)[0]  # 解析报头数据
    # 3、结收真实数据
    recv_size = 0
    recv_data = b''

    while recv_size < total_size:  # 收数据，知道收完
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)
    print(recv_data.decode('GB2312'))

phone.close()


