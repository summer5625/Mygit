# -*- coding: utf-8 -*-
# @Time    : 2019/6/16  11:03
# @Author  : XiaTian
# @File    : 客户.py

import struct
import json
from socket import *
from threading import Thread, currentThread

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8071))


def head_dict(sock, data):

        head_json = json.dumps(data)
        head_bytes = head_json.encode('utf-8')

        # 发送报头长度
        head_len = struct.pack('i', len(head_bytes))
        sock.send(head_len)
        # 发送报头
        sock.send(head_bytes)


def run():
    while True:
        msg = input('>>:').strip()
        if not msg:continue
        head_dict(client, msg)
        data = client.recv(1024)
        print(data.decode('utf-8'))

    # client.close()


run()
