# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 22:50
# @Author  : XiaTian
# @File    : servers.py

import socket
import struct
import json
import os

from conf import setting


class Client:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    path = setting.BASIS_DIR
    function = [
        ('退出', 'close_connect'),
        ('密码修改', 'change_pwd'),
        ('充值金额', 'recharge'),
        ('扩充容量', 'dilatation'),
        ('文件查看', 'look_file'),
        ('文件上传', 'uploading')
    ]

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if connect:
            try:
                self.client_connect()
            except BaseException:
                self.close_connect()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def close_connect(self):
        self.socket.close()
        exit()

    # 用户登录认证
    def login(self, cmd):

        count = 0
        id_list = []                                            # 输入ID列表
        while count < 3:
            user_id = input('请输入ID>>:').strip()
            user_password = input('请输入密码>>:').strip()
            id_list.append(user_id)

            if id_list.count(user_id) < 3:
                send_msg = {
                    'cmd': cmd,
                    'user_id': user_id,
                    'user_password': user_password,
                    'count': id_list.count(user_id)
                }
                self.head_dict(send_msg)                        # 发送报头

                rcv = self.socket.recv(setting.Packet_Size)
                # 将从服务端接收到的信息转换成字典
                info = eval(rcv)

                if len(info) != 0:                              # 从服务端拿到字典为空则继续尝试登陆
                    if info['state'] == '0':
                        print('\033[0;36m登陆成功!\033[0m')
                        return info                             # 登录成功返回用户个人信息
                    else:
                        print('\033[31m账号被冻结!\033[0m')
                        self.close_connect()
                else:
                    print('\033[31m账号或者密码错误!\033[0m')
                    count += 1
            else:                                              # 同一个用户名在同一个客户端密码连续输出3次账号锁定
                send_msg = {
                    'cmd': cmd,
                    'user_id': user_id,
                    'count': id_list.count(user_id)
                }
                self.head_dict(send_msg)
                print('错误次数过多，%s账号已被冻结!' % user_id)
                self.close_connect()

    # 新用户注册
    def add_user(self, cmd):
        while True:
            user_name = input('请设置用户名>>:').strip()
            user_password = input('请设置密码>>:').strip()
            send_msg = {
                'cmd': cmd,
                'user_name': user_name,
                'user_password': user_password
            }
            self.head_dict(send_msg)
            rcv = self.socket.recv(setting.Packet_Size)
            info = eval(rcv.decode(setting.CODING))              # 发送服务器注册信息
            if len(info) != 0:
                os.makedirs(
                    r'%s\client\%s\download' %
                    (setting.BASIS_DIR, user_name))  # 创建下载路径
                print('\033[0;36m注册成功!\033[0m')
                self.run(info)
            else:
                print('\033[31m用户名重复或者为空!\033[0m')

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
        head_bytes = head_json.encode(setting.CODING)

        # 发送报头长度
        head_len = struct.pack('i', len(head_bytes))
        self.socket.send(head_len)

        # 发送报头
        self.socket.send(head_bytes)

    # 修改密码
    def change_pwd(self, cmd, info):
        old_pwd = input('请输入旧密码>>:').strip()
        if old_pwd == info['password']:
            new_pwd = input('请输入新密码>>:').strip()
            data = {
                'user_id': info['user_id'],
                'cmd': cmd,
                'old_pwd': old_pwd,
                'new_pwd': new_pwd
            }
            self.head_dict(data)
            print('\033[0;36m密码修改成功!\033[0m')
        else:
            print('\033[31m密码错误!\033[0m')

    # 充值金额
    def recharge(self, cmd, info):
        while True:
            print('当前余额:%s' % info['balance'])
            money = input('请输入充值金额>>:').strip()
            if money.isdigit():
                money = int(money)
                send_msg = {
                    'user_id': info['user_id'],
                    'cmd': cmd,
                    'money': money
                }
                self.head_dict(send_msg)
                new_balance = self.socket.recv(setting.Packet_Size)
                print(
                    '\033[0;36m充值成功,当前余额%s!\033[0m' %
                    new_balance.decode(
                        setting.CODING))
                return
            else:
                print('\033[31m请输入正确的数字!\033[0m')

    # 扩容
    def dilatation(self, cmd, info):
        while True:

            print('\033[0;33m1GB/50RMB,请输入整数!\033[0m')
            print('总空间:%s  已用空间:%s' % (info['memory'], info['use_space']))
            buy_memory = input('请输入购买容量>>:').strip()

            if buy_memory.isdigit():
                need_money = int(buy_memory) * 50
                buy_memory = int(buy_memory)
                send_msg = {
                    'cmd': cmd,
                    'user_id': info['user_id'],
                    'buy_memory': buy_memory,
                    'need_money': need_money
                }

                self.head_dict(send_msg)
            else:
                print('\033[31m请输入整数!\033[0m')
                continue

            recv_msg = self.socket.recv(setting.Packet_Size)
            new_msg = eval(recv_msg.decode(setting.CODING))
            if new_msg['flag']:
                print('\033[0;36m交易成功!\033[0m')
                print('\033[0;36m总空间:%s  余额:%s\033[0m' %
                      (new_msg['new_memory'], new_msg['new_balance']))
                return
            else:
                print('\033[31m余额不足，请充值!\033[0m')
                print('\033[31m当前余额: %s \033[0m' % new_msg['new_balance'])

    # 上传文件
    def uploading(self, cmd, info):
        while True:
            file_path = input('输入上传文件路径>>:').strip()
            if os.path.isfile(r'%s' % (file_path)):
                send_msg = {
                    'cmd': cmd,
                    'user_id': info['user_id'],
                    'file_path': r'%s' % (file_path),
                    'file_size': os.path.getsize(r'%s' % (file_path))
                }
                self.head_dict(send_msg)   # 发送报头
            else:
                print('\033[31m文件不存在!\033[0m')
                continue
            recv = self.socket.recv(setting.Packet_Size)
            recv_dict = eval(recv.decode(setting.CODING))  # 接收来自服务器返回的消息
            if recv_dict['flag']:                          # 文件超过剩余容量不上传
                with open(r'%s' % (file_path), 'rb') as f:
                    for line in f:
                        self.socket.send(line)
                print('\033[0;36m上传成功!\033[0m')
                print('\033[31m内存已使用:%s!\033[0m' % recv_dict['use_space'])
                return
            else:
                print(
                    '\033[31m内存不足,剩余内存:%s!\033[0m' %
                    recv_dict['surplus_space'])
                return

    # 文件下载
    def download(self, user_id, file_path):
        send_msg = {
            'cmd': 'download',
            'user_id': user_id,
            'file_path': file_path
        }
        self.head_dict(send_msg)
        obj = self.socket.recv(4)
        header_size = struct.unpack('i', obj)[0]

        header_bytes = self.socket.recv(header_size)

        header_json = header_bytes.decode(setting.CODING)
        header_dict = json.loads(header_json)

        file_size = header_dict['file_size']
        filename = header_dict['filename'].split('\\')
        download_path = r'%s\client\%s\%s' % (
            setting.BASIS_DIR, user_id, filename[-1])
        with open(download_path, 'wb') as f:
            recv_size = 0
            while recv_size < file_size:  # 收数据，直到收完
                line = self.socket.recv(1024)
                f.write(line)
                recv_size += len(line)
                print('总大小:%s    已下载大小:%s' % (file_size, recv_size))

    # 浏览家目录
    def look_file(self, cmd, info):
        send_msg = {
            'cmd': cmd,
            'user_id': info['user_id']
        }
        self.head_dict(send_msg)
        while True:
            recv = self.socket.recv(setting.Packet_Size)
            recv_dict = eval(recv.decode(setting.CODING))
            file_list = recv_dict['file_list']  # 结束来自服务器的消息
            while True:
                if recv_dict['end_flag']:       # 服务器端发送的结束标志
                    return
                if recv_dict['is_file']:        # 服务器端判断用户选择内容是否是文件，是文件则直接下载，文件夹则直接进入文件夹
                    print(recv_dict['file_path'])
                    return self.download(
                        info['user_id'], recv_dict['file_path'])  # 下载文件
                for index, i in enumerate(file_list):
                    print(index, i)
                choice = input('请选择文件>>:').strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice < len(file_list):
                        self.socket.send(str(choice).encode(setting.CODING))
                        break
                    else:
                        print('\033[31m请输入正确的序号!\033[0m')
                        continue
                elif choice == 'q' or choice == 'b':
                    self.socket.send(str(choice).encode(setting.CODING))
                    break
                else:
                    print('\033[31m请输入正确的序号!\033[0m')
                    continue


def main():
    obj = Client(setting.IP)
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
