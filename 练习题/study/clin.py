# -*- coding: utf-8 -*-
# @Time    : 2019/7/2  23:37
# @Author  : XiaTian
# @File    : clin.py

import socket
import struct
import json
import os


class Client:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    path = os.path.dirname(os.path.abspath(__file__))
    function = [
        ('退出', 'close_connect'),
        ('密码修改', 'change_pwd'),
        ('充值金额', 'recharge'),
        ('扩充容量', 'dilatation'),
        ('文件查看', 'look_file'),
        ('文件上传', 'uploading')
    ]

    def __init__(self, server_address, ):  # connect=True
        self.server_address = server_address
        self.client = socket.socket(self.address_family,
                                    self.socket_type)

        self.client.connect(self.server_address)
        # if connect:
        #     try:
        #         self.client_connect()
        #     except BaseException:
        #         self.close_connect()
        #         raise

    # def client_connect(self):
    #     self.socket.connect(self.server_address)

    def close_connect(self):
        self.client.close()
        exit()

    # 功能分发
    def run(self, info):
        while True:
            for index, i in enumerate(self.function):
                print(index, i[0])
            choice = input('请选择操作>>:').strip()
            if choice.isdigit():
                choice = int(choice)
            else:
                print('\033[31m请输入正确的序号!\033[0m')
                continue

            if choice < len(self.function):
                if hasattr(self, self.function[choice][1]):
                    if self.function[choice][1] == 'close_connect':
                        getattr(self, self.function[choice][1])()
                    else:
                        func = getattr(self, self.function[choice][1])
                        func(self.function[choice][1], info)
            else:
                print('\033[31m请输入正确的序号!\033[0m')

    # 发送报头
    def head_dict(self, data):
        head_json = json.dumps(data)
        head_bytes = head_json.encode('utf-8')

        # 发送报头长度
        head_len = struct.pack('i', len(head_bytes))
        self.client.send(head_len)
        print(1)
        # 发送报头
        self.client.send(head_bytes)
        print(2)

    # 用户登录认证
    def login(self, cmd):

        id_list = []                                            # 输入ID列表
        while True:
            user_id = input('请输入ID>>:').strip()
            user_password = input('请输入密码>>:').strip()
            id_list.append(user_id)
            send_msg = {
                'cmd': cmd,
                'user_id': user_id,
                'user_password': user_password,
                'count': id_list.count(user_id)
            }

            self.head_dict(send_msg)                        # 发送报头
            rcv = self.client.recv(1024)     # 接收服务器返回数据
            info = json.loads(rcv)
            print(info)
            if info['state_code'] == 100:
                print('%s' % info['respond_msg'])
                return user_id
            else:
                print('%s' % info['respond_msg'])

    def change_pwd(self, cmd ,info):
        print(cmd, info)


def main():
    obj = Client(('127.0.0.1', 8070))
    while True:
        fun_list = [
            ('登录', 'login'),
            ('注册', 'add_user')
        ]
        for index, i in enumerate(fun_list):
            print(index, i[0])
        choice = input('请选择操作>>:').strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print('\033[31m请输入正确的序号!\033[0m')
            continue
        if choice < len(fun_list):
            if hasattr(obj, fun_list[choice][1]):
                user = getattr(obj, fun_list[choice][1])(fun_list[choice][1])
                obj.run(user)
        else:
            print('\033[31m请输入正确的序号!\033[0m')

    obj.client.close()


main()