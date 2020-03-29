# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 22:50
# @Author  : XiaTian
# @File    : servers.py

import socket
import struct
import json
import os
import re
import configparser

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
        ('文件上传', 'uploading'),
        ('文件下载', 'download'),
        ('查看未下载完成任务', 'show_undone_task'),
        ('删除文件', 'del_file')
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
            rcv = self.socket.recv(setting.Packet_Size)     # 接收服务器返回数据
            info = json.loads(rcv)
            if info['state_code'] == 100:
                print('%s' % info['respond_msg'])
                info.pop('state_code')
                info.pop('respond_msg')
                return info
            else:
                print('%s' % info['respond_msg'])

    # 新用户注册
    def add_user(self, cmd):
        while True:
            user_name = input('请设置用户名>>:').strip()
            user_password = input('请设置密码>>:').strip()
            if len(user_name) != 0 and len(user_password) != 0:
                send_msg = {
                    'cmd': cmd,
                    'user_name': user_name,
                    'user_password': user_password
                }
                self.head_dict(send_msg)
                rcv = self.socket.recv(setting.Packet_Size)
                info = json.loads(rcv.decode(setting.CODING)
                                  )              # 发送服务器注册信息

                if info['state_code'] == 200:
                    print('\033[0;36m%s\033[0m' % info['respond_msg'])
                    info['user_id'] = user_name
                    info['password'] = user_password
                    get_msg = self.login('login')  # 注册成功，登录
                    return get_msg

                else:
                    print('\033[31m%s\033[0m' % info['respond_msg'])
            else:
                print('\033[31m账号名和密码不能为空!\033[0m')

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
            money = input('请输入充值金额|b,返回上级|q，退出>>:').strip()
            if money.isdigit():
                money = int(money)
                send_msg = {
                    'user_id': info['user_id'],
                    'cmd': cmd,
                    'money': money
                }
                self.head_dict(send_msg)
                recv = self.socket.recv(setting.Packet_Size)
                info = json.loads(recv.decode(setting.CODING))
                print(
                    '\033[0;36m%s,当前余额%s!\033[0m' %
                    (info['respond_msg'], info['balance']))
            elif money == 'q' or money == 'Q':
                self.close_connect()
            elif money == 'b' or money == 'B':
                return
            else:
                print('\033[31m请输入正确的数字!\033[0m')

    # 扩容
    def dilatation(self, cmd, info):
        while True:

            print('\033[0;33m1GB/50RMB,请输入整数!\033[0m')
            print('总空间:%s  已用空间:%s' % (info['memory'], info['use_space']))
            buy_memory = input('请输入购买容量|b,返回上级|q，退出>>:').strip()

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
            elif buy_memory == 'q' or buy_memory == 'Q':
                self.close_connect()
            elif buy_memory == 'b' or buy_memory == 'B':
                return
            else:
                print('\033[31m请输入整数!\033[0m')
                continue

            recv_msg = self.socket.recv(setting.Packet_Size)
            new_msg = json.loads(recv_msg.decode(setting.CODING))
            if new_msg['state_code'] == 302:
                print('\033[0;36m%s!\033[0m' % new_msg['respond_msg'])
                print('\033[0;36m总空间:%s  余额:%s\033[0m' %
                      (new_msg['new_memory'], new_msg['new_balance']))
                return
            else:
                print('\033[31m%s，请充值!\033[0m' % new_msg['respond_msg'])
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
            recv_dict = json.loads(recv.decode(setting.CODING))  # 接收来自服务器返回的消息
            if recv_dict['flag']:                          # 文件超过剩余容量不上传
                send_size = 0
                last_percent = 0
                with open(r'%s' % (file_path), 'rb') as f:
                    for line in f:
                        self.socket.send(line)
                        send_size += len(line)
                        current_percent = int(
                            send_size / send_msg['file_size']) * 100
                        if current_percent > last_percent:
                            print(
                                '|' *
                                current_percent +
                                '{}%'.format(current_percent))
                        last_percent = current_percent
                print('\033[0;36m上传成功!\033[0m')
                print('\033[31m内存已使用:%s!\033[0m' % recv_dict['use_space'])
                return
            else:
                print(
                    '\033[31m内存不足,剩余内存:%s!\033[0m' %
                    recv_dict['surplus_space'])
                return

    # 检查下载文件是否有重复
    def check_file(self, file_name):
        check_dir = self.check_down_path()
        file_list = os.listdir(check_dir)
        same_file = []
        for i in file_list:
            if i.startswith(file_name):
                same_file.append(i)
        return len(same_file)

    # 获取记录的所有下载文件的基本信息
    def get_record(self):
        record_path = r'%s\core\download.ini' % self.path
        if os.path.exists(record_path):

            config = configparser.ConfigParser()
            config.read(record_path, encoding=setting.CODING)
        else:
            with open(record_path, 'w') as f:
                f.write('')
                f.close()
            config = configparser.ConfigParser()
            config .read(record_path, encoding=setting.CODING)

        return config

    # 将下载文件信息写进文件中
    def storage_record_config(self, file_msg):
        record_conf = self.get_record()
        record_conf.add_section(file_msg['new_file_name'])
        record_conf[file_msg['new_file_name']
                    ]['file_name'] = file_msg['file_name']
        record_conf[file_msg['new_file_name']
                    ]['server_file_path'] = file_msg['server_file_path']
        record_conf[file_msg['new_file_name']
                    ]['total_size'] = str(file_msg['total_size'])
        record_conf.write(
            open(
                r'%s\core\download.ini' %
                self.path,
                'w',
                encoding=setting.CODING))

    # 文件下载
    def download(self, cmd, info):
        file_msg = {}
        download_file = self.look_file('look_file', info)
        try:
            file_msg['user_id'] = info['user_id']
            file_msg['server_file_path'] = download_file
            file_msg['recv_size'] = 0
            file_name = download_file.split('\\')[-1]
            count = self.check_file(file_name)
            if count == 0:
                file_msg['file_name'] = file_name
                file_msg['new_file_name'] = '%s.temp' % file_name
                self.transmit_file(file_msg)
            else:
                file_msg['file_name'] = file_name
                file_msg['new_file_name'] = '{0}.{1}.temp'.format(
                    file_name, count)
                self.transmit_file(file_msg)
        except Exception:
            return

    # 接收来自服务端发来的下载数据
    def transmit_file(self, file_msg):
        record_conf = self.get_record()
        send_msg = file_msg
        send_msg['cmd'] = 'download'
        self.head_dict(send_msg)
        obj = self.socket.recv(4)
        header_size = struct.unpack('i', obj)[0]
        header_bytes = self.socket.recv(header_size)

        header_json = header_bytes.decode(setting.CODING)
        header_dict = json.loads(header_json)
        if header_dict['state_code'] == 401:
            file_size = header_dict['file_size']
            file_msg['total_size'] = file_size
            if file_msg['new_file_name'] not in record_conf.sections():
                self.storage_record_config(file_msg)

            filename = file_msg['new_file_name']
            dow_path = self.check_down_path()
            download_path = r'%s\%s' % (dow_path, filename)
            with open(download_path, 'ab') as f:
                recv_size = send_msg['recv_size']
                last_percent = 0
                while recv_size < file_size:  # 收数据，直到收完
                    line = self.socket.recv(1024)
                    f.write(line)
                    recv_size += len(line)
                    current_percent = int(recv_size / file_size) * 100
                    if current_percent > last_percent:
                        print(
                            '|' *
                            current_percent +
                            '{}%'.format(current_percent),
                            end='\r',
                            flush=True)
                    last_percent = current_percent
                    # print('总大小:%s    已下载大小:%s' % (file_size, recv_size))

            if recv_size == file_size:
                real_name = filename[:-5]
                new_path = r'{}\{}'.format(dow_path, real_name)
                os.rename(download_path, new_path)
                print('\n')
                print('\033[0;36m下载成功!\033[0m')
        else:
            print('\033[31m%s\033[0m' % header_dict['respond_msg'])

    # 检查下载路径是否存在
    def check_down_path(self):
        down_path = r'%s\download' % self.path
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        return down_path

    # 查看未下载完成的任务
    def show_undone_task(self, cmd, info):
        check_path = self.check_down_path()
        file_list = os.listdir(check_path)
        record_conf = self.get_record()
        file_msg = {}
        undone_file = []
        for i in file_list:
            if i.endswith('.temp'):
                undone_file.append(i)
        if len(undone_file) != 0:
            for index, k in enumerate(undone_file):

                client_path = r'%s\%s' % (check_path, k)
                total = int(record_conf[k]['total_size'])
                real_size = os.path.getsize(client_path)
                rate = (round(real_size / total, 3)) * 100
                print('{0} {1} 已下载:{2}%'.format(index, k, rate))
        else:
            print('这里空空如也!')
            return

        choice = input('选择继续下载任务|q,退出程序|b,返回主菜单:').strip()
        if choice.isdigit():
            choice = int(choice)
            key_name = undone_file[choice]
            file_msg['user_id'] = info['user_id']
            file_msg['server_file_path'] = record_conf[key_name]['server_file_path']
            file_dir = r'%s\%s' % (check_path, key_name)
            file_msg['recv_size'] = os.path.getsize(file_dir)
            file_msg['new_file_name'] = key_name
            file_msg['file_name'] = record_conf[key_name]['file_name']

            return self.transmit_file(file_msg)  # 接着下载文件

        elif choice == 'q' or choice == 'Q':
            self.close_connect()

        elif choice == 'b' or choice == 'B':
            return

        else:
            print('\033[31m请输入正确的数字!\033[0m')

    # 浏览家目录
    def look_file(self, cmd, info):
        send_msg = {
            'cmd': cmd,
            'user_id': info['user_id']
        }
        self.head_dict(send_msg)
        while True:
            recv = self.socket.recv(setting.Packet_Size)
            recv_dict = json.loads(recv.decode(setting.CODING))
            file_list = recv_dict['file_list']  # 接收来自服务器的消息
            while True:
                if recv_dict['end_flag']:       # 服务器端发送的结束标志
                    return
                if recv_dict['is_file']:        # 服务器端判断用户选择内容是否是文件，是文件则直接下载，文件夹则直接进入文件夹
                    return recv_dict['file_path']  # 返回文件所在路径
                for index, i in enumerate(file_list):
                    print(index, i)
                choice = input('请选择文件>>:').strip()
                if choice.isdigit():
                    if int(choice) < len(file_list):
                        self.socket.send(
                            json.dumps(choice).encode(
                                setting.CODING))
                        break
                    else:
                        print('\033[31m请输入正确的序号!\033[0m')
                        continue
                elif choice == 'B' or choice == 'b':
                    self.socket.send(json.dumps(choice).encode(setting.CODING))
                    break
                elif choice == 'Q' or choice == 'q':
                    self.socket.send(json.dumps(choice).encode(setting.CODING))
                    break
                else:
                    print('\033[31m请输入正确的序号!\033[0m')
                    continue

    # 删除文件
    def del_file(self, cmd, info):
        pick_file = self.look_file('look_file', info)
        if pick_file is not None:
            send_msg = {
                'cmd': cmd,
                'file_path': pick_file,
                'user_id': info['user_id']}
            self.head_dict(send_msg)

            rec_data = self.socket.recv(setting.Packet_Size)
            recv_dict = json.loads(rec_data.decode(setting.CODING))
            if recv_dict['state_code'] == 402:
                print(
                    '\033[31m{}{}\033[0m'.format(
                        recv_dict['file_name'],
                        recv_dict['respond_msg']))
                print(
                    '\033[0;36m成功释放{}内存!\033[0m'.format(
                        recv_dict['file_size']))


def main():
    obj = Client(setting.IP)
    while True:
        fun_list = [
            ('登陆', 'login'),
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

    obj.socket.close()
