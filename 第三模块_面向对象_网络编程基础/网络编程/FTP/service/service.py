# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 22:50
# @Author  : XiaTian
# @File    : server.py

import socket
import struct
import os
import configparser
import json

from conf import setting
from core.logger import Logger


class Service:

    address_family = socket.AF_INET        # 套接字家族
    address_type = socket.SOCK_STREAM      # 套接字类型
    path = setting.BASIS_DIR               # 获取程序的根目录
    allow_reuse_address = False

    def __init__(self, server_address, bind_and_active=True):
        self.server_address = server_address
        print(server_address, type(server_address))
        self.socket = socket.socket(self.address_family, self.address_type)
        if bind_and_active:
            try:
                self.server_bind()         # 绑定IP和端口
                self.server_activate()     #
            except BaseException:
                self.server_close()        # 没被激活，则关闭
                raise

    #  绑定IP和端口
    def server_bind(self):
        if self.allow_reuse_address:  # 判断ip和端口是否能被重用
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)  # 绑定IP和端口
        self.server_address = self.socket.getsockname()  # 获取当前的地址

    # 监听
    def server_activate(self):
        self.socket.listen(5)

    def server_close(self):
        self.socket.close()  # 关闭套接字

    def get_request(self):
        return self.socket.accept()   # 与客户端握手建立连接

    def close_connect(self, request):
        request.close()

    # 获取用户信息
    def get_file(self):

        file_path = r'%s\db\user_info.ini' % self.path      # 获取打开文件的路径
        if os.path.exists(file_path):

            conf = configparser.ConfigParser()
            conf.read(file_path, encoding=setting.CODING)
        else:
            with open(file_path, 'w') as f:
                f.write('')
                f.close()
            conf = configparser.ConfigParser()
            conf.read(file_path, encoding=setting.CODING)

        return conf                                          # 返回文件内容

    # 用户注册
    def add_user(self, st):
        msg_dict = eval(st)
        user_info = self.get_file()
        user_id = msg_dict['user_name']
        send_dict = {}
        if user_id not in user_info.sections() and len(user_id) != 0:

            user_info.add_section(msg_dict['user_name'])
            user_info[user_id]['state'] = '0'
            user_info[user_id]['password'] = msg_dict['user_password']
            user_info[user_id]['home_dir'] = str(setting.Home_Dir(user_id))
            os.makedirs(str(setting.Home_Dir(user_id)))             # 生成个人家目录
            os.makedirs(r'%s\share' %
                        str(setting.Home_Dir(user_id)))  # 生成上传文件夹
            # 注册后个人存储空间为1G
            user_info[user_id]['memory'] = '1G'
            user_info[user_id]['use_space'] = '0'
            user_info[user_id]['balance'] = '0'
            user_info.write(
                open(
                    r'%s\db\user_info.ini' %
                    self.path,
                    'w',
                    encoding=setting.CODING))

            send_dict['user_id'] = user_id
            send_dict['state'] = '0'
            send_dict['password'] = msg_dict['user_password']
            send_dict['home_dir'] = user_info[user_id]['home_dir']
            send_dict['memory'] = '1G'
            send_dict['use_space'] = '0'
            send_dict['balance'] = '0'
            self.conn.send(
                str(send_dict).encode(
                    setting.CODING))   # 用户注册信息返回给客户端

            log_msg = 'account:%s  operation:add_user  info:registered successfully' % user_id
            loggers = Logger.logs('operation')
            loggers.info(log_msg)           # 记录日志

        else:
            self.conn.send(str(send_dict).encode(setting.CODING))

    # 用户登录验证
    def login(self, st):

        msg_dict = eval(st)             # 获取从报头中解析出来的信息

        user_info = self.get_file()     # 从数据库中获取用户信息

        send_dict = {}
        if msg_dict['count'] < 3:
            if msg_dict['user_id'] in user_info.sections():
                password = user_info[msg_dict['user_id']]['password']
            if msg_dict['user_password'] == password:
                for k, v in user_info[msg_dict['user_id']].items():
                    send_dict[k] = v
                send_dict['user_id'] = msg_dict['user_id']
                self.conn.send(
                    str(send_dict).encode(
                        setting.CODING))  # 账号密码正确向客户端发送用户信息

                log_msg = 'account:%s  operation:login  info:login successfully' % msg_dict[
                    'user_id']
                loggers = Logger.logs('landing')
                loggers.info(log_msg)  # 记录日志

            else:
                self.conn.send(str(send_dict).encode(setting.CODING))
        else:   # 用户密码输出超过三次账号冻结
            user_info[msg_dict['user_id']]['state'] = '1'
            user_info.write(
                open(
                    r'%s\db\user_info.ini' %
                    self.path,
                    'w',
                    encoding=setting.CODING))  # 密码输出3次以上账号冻结

            log_msg = 'account:%s  operation:login  info:account lockout' % msg_dict['user_id']
            loggers = Logger.logs('landing')
            loggers.info(log_msg)  # 记录日志

    # 功能分发
    def run(self):
        while True:
            self.conn, self.client_addr = self.get_request()
            print('from servers ', self.client_addr)
            while True:
                try:
                    obj = self.conn.recv(4)
                    head_size = struct.unpack('i', obj)[0]  # 解析客户端发送的报头
                    msg_dict = self.conn.recv(head_size)
                    header_json = msg_dict.decode(setting.CODING)
                    header_dict = json.loads(header_json)
                    if hasattr(self, header_dict['cmd']):
                        game = getattr(self, header_dict['cmd'])
                        game(str(header_dict))

                except Exception:
                    break

    # 修改密码
    def change_pwd(self, st):
        msg_dict = eval(st)  # 获取从报头中解析出来的信息
        user_info = self.get_file()  # 从数据库中获取用户信息
        user_id = msg_dict['user_id']
        if user_info[user_id]['password'] == msg_dict['old_pwd']:
            user_info[user_id]['password'] = msg_dict['new_pwd']
            user_info.write(
                open(
                    r'%s\db\user_info.ini' %
                    self.path,
                    'w',
                    encoding=setting.CODING))

            log_msg = 'account:%s  operation:change password  info:change password successfully' % user_id
            loggers = Logger.logs('landing')
            loggers.info(log_msg)  # 记录日志

    # 充值金额
    def recharge(self, st):
        msg_dict = eval(st)
        user_info = self.get_file()
        user_id = msg_dict['user_id']
        user_info[user_id]['balance'] = str(
            int(user_info[user_id]['balance']) + msg_dict['money'])
        user_info.write(
            open(
                r'%s\db\user_info.ini' %
                self.path,
                'w',
                encoding=setting.CODING))
        new_info = self.get_file()
        back_msg = new_info[user_id]['balance']
        self.conn.send(back_msg.encode(setting.CODING))  # 充值成功返回一个成功状态给客户端

        log_msg = 'account:%s  operation:recharge  recharge_money:%s  info:recharge successfully' % \
                  (user_id, msg_dict['money'])
        loggers = Logger.logs('transaction')
        loggers.info(log_msg)  # 记录日志

    # 文件内存转换
    def bytes(self, bytes):
        if bytes < 1024:  # 比特
            bytes = str(round(bytes, 2)) + ' B'  # 字节
        elif bytes >= 1024 and bytes < 1024 * 1024:
            bytes = str(round(bytes / 1024, 2)) + ' KB'  # 千字节
        elif bytes >= 1024 * 1024 and bytes < 1024 * 1024 * 1024:
            bytes = str(round(bytes / 1024 / 1024, 2)) + ' MB'  # 兆字节
        else:
            bytes = str(round(bytes / 1024 / 1024 / 1024, 2)) + ' GB'  # 千兆字节

        return bytes

    # 个人空间使用大小
    def space_calculate(self, user_id):
        total_size = 0
        user_msg = self.get_file()
        file_list = os.walk(
            user_msg[user_id]['home_dir'],
            topdown=False)  # 获取指定目录下的文件夹列表
        for root, dirs, files in file_list:
            for name in files:
                file_size = os.path.getsize(os.path.join(
                    root, name))  # 将文件和所在文件夹名称拼接成文件路径并计算文件大小
                total_size = total_size + file_size
        total_size = self.bytes(total_size)

        return total_size

    # 购买存储空间
    def dilatation(self, st):
        msg_dict = eval(st)
        user_info = self.get_file()
        user_id = msg_dict['user_id']
        if int(user_info[user_id]['balance']) >= msg_dict['need_money']:
            new_memory = int(user_info[user_id]['memory'].split('G')[
                             0]) + int(msg_dict['buy_memory'])
            balance = int(user_info[user_id]['balance']
                          ) - msg_dict['need_money']
            user_info[user_id]['balance'] = str(balance)
            user_info[user_id]['memory'] = str(new_memory) + 'GB'
            user_info.write(
                open(
                    r'%s\db\user_info.ini' %
                    self.path,
                    'w',
                    encoding=setting.CODING))
            send_msg = {
                'flag': True,
                'new_memory': str(new_memory) + 'GB',
                'new_balance': balance
            }
            self.conn.send(
                str(send_msg).encode(
                    setting.CODING))  # 充值成功返回客户端状态信息

            log_msg = 'account:%s  operation:dilatation  buy_spacey:%s  info:dilatation successfully' % \
                      (user_id, str(msg_dict['buy_memory']) + 'G')
            loggers = Logger.logs('transaction')
            loggers.info(log_msg)  # 记录日志

        else:
            send_msg = {
                'flag': False,
                'new_memory': user_info[user_id]['memory'],
                'new_balance': user_info[user_id]['balance']
            }
            self.conn.send(str(send_msg).encode(setting.CODING))

    # 获取指定路径下文件列表
    def get_path(self, dir_path, root_dir, send_dict):

        file_list = os.listdir(dir_path)  # 获取客户端选择指定目录下的所有文件和文件夹
        send_dict['file_list'] = file_list
        self.conn.send(str(send_dict).encode(setting.CODING))  # 将获得的文件列表返回给客户端
        while True:
            recv = self.conn.recv(setting.Packet_Size)
            choice = recv.decode(setting.CODING)
            if choice.isdigit():
                choice = int(choice)
                if choice < len(file_list):
                    file_path = os.path.join(
                        dir_path, file_list[choice])  # 将选择的文件和所在路径拼接
                    if os.path.isfile(
                            file_path):                         # 指定路径是文件则返回给客户端文件名，并下载文件
                        send_dict['file_path'] = file_path
                        send_dict['is_file'] = True
                        self.conn.send(str(send_dict).encode(setting.CODING))
                        return
                    # 选择路径下时文件夹则进入文件夹
                    elif os.path.isdir(file_path):
                        return self.get_path(file_path, root_dir, send_dict)
                else:
                    return self.get_path(
                        dir_path, root_dir, send_dict)    # 选择不存在，返回当前文件夹
            elif choice == 'b':                                          # 返回上一级目录
                if dir_path == root_dir:                                 # 如果返回路径是个人家目录，则显示家目录
                    return self.get_path(dir_path, root_dir, send_dict)
                else:
                    file_path = os.path.dirname(
                        dir_path)                # 不是家目录则回退一级目录
                    return self.get_path(file_path, root_dir, send_dict)
            elif choice == 'q':
                send_dict['end_flag'] = True
                self.conn.send(
                    str(send_dict).encode(
                        setting.CODING))    # 退出文件浏览
                return

    # 浏览文件，访问家目录
    def look_file(self, st):
        msg_dict = eval(st)
        user_info = self.get_file()
        user_id = msg_dict['user_id']
        file_path = user_info[user_id]['home_dir']
        send_dict = {
            'end_flag': False,
            'is_file': False,
            'file_list': None,
            'file_path': None
        }
        self.get_path(file_path, file_path, send_dict)

    # 下载文件
    def download(self, st):
        msg_dict = eval(st)
        user_id = msg_dict['user_id']

        header_dict = {
            'filename': msg_dict['file_path'],
            'md5': 'xxxx',
            'file_size': os.path.getsize(r'%s' % msg_dict['file_path'])
        }          # 制作报头
        header_json = json.dumps(header_dict)
        header_bytes = header_json.encode(setting.CODING)

        self.conn.send(struct.pack('i', len(header_bytes)))  # 发送报头长度
        self.conn.send(header_bytes)                         # 发送报头

        with open(r'%s' % msg_dict['file_path'], 'rb') as f:  # 发送下载文件内容
            for line in f:
                self.conn.send(line)

        file_list = msg_dict['file_path'].split('\\')
        log_msg = 'account:%s  operation:download  file_name:%s  info:download successfully' % \
                  (user_id, file_list[-1])
        loggers = Logger.logs('operation')
        loggers.info(log_msg)  # 记录日志

    # 上传文件
    def uploading(self, st):
        msg_dict = eval(st)
        user_info = self.get_file()
        user_id = msg_dict['user_id']
        total_size = int(user_info[user_id]['memory'].split('G')[0])
        total_v = total_size * 1024 * 1024 * 1024
        file_name = msg_dict['file_path'].split('\\')
        send_msg = {
            'flag': True,
            'use_space': None,
            'surplus_space': None,
            'file_size': self.bytes(msg_dict['file_size'])
        }      # 发送给客户端的状态信息
        if int(user_info[user_id]['use_space']) + \
                msg_dict['file_size'] <= total_v:  # 判断文件大小是否超过内存
            use_space = int(
                user_info[user_id]['use_space']) + msg_dict['file_size']
            user_info[user_id]['use_space'] = str(use_space)
            user_info.write(
                open(
                    r'%s\db\user_info.ini' %
                    self.path,
                    'w',
                    encoding=setting.CODING))
            send_msg['use_space'] = self.bytes(use_space)
            uploading_path = r'%s\service\file_path\%s\share\%s' % (
                setting.BASIS_DIR, user_id, file_name[-1])
            self.conn.send(str(send_msg).encode(setting.CODING))
            with open(uploading_path, 'wb') as f:
                print(uploading_path)
                recv_size = 0
                while recv_size < msg_dict['file_size']:
                    line = self.conn.recv(1024)
                    f.write(line)
                    recv_size += len(line)
                    print(
                        '总大小:%s    已上传大小:%s' %
                        (msg_dict['file_size'], recv_size))

            log_msg = 'account:%s  operation:uploading  file_name:%s  info:uploading successfully' % \
                      (user_id, file_name[-1])
            loggers = Logger.logs('operation')
            loggers.info(log_msg)  # 记录日志

        else:
            surplus_space = total_v - int(user_info[user_id]['use_space'])
            send_msg['flag'] = False
            send_msg['surplus_space'] = self.bytes(surplus_space)
            self.conn.send(str(send_msg).encode(setting.CODING))


def main():

    client = Service(setting.IP)
    client.run()
