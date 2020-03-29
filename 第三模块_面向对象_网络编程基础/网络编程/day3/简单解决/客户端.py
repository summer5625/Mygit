# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 客户端.py

import socket
import struct
import json


phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    cmd = input('>>:').strip()

    # 发命令
    phone.send(cmd.encode('utf-8'))

    # 1、先拿报头长度
    obj = phone.recv(4)
    header_size = struct.unpack('i',obj)[0]

    # 2、收报头
    header_bytes = phone.recv(header_size)

    # 3、从报头解析真实数据信息
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    print(header_dict)
    total_size = header_dict['total_size']

    # 4、接收真实数据
    recv_size = 0
    recv_data = b''

    while recv_size < total_size:  # 收数据，知道收完
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)
    print(recv_data.decode('GB2312'))

phone.close()


