# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 22:50
# @Author  : XiaTian
# @File    : server.py
from socket import *
import struct
import os
import re
import configparser
import json

from conf import setting
from core.logger import Logger
from core import threadpool


class Service:

    STATE_CODE = {100: '登录成功!', 101: '账号或者密码错误', 102: '账号被冻结',
                  201: '账号已存在!', 200: '注册成功!',
                  300: '充值成功!', 301: '余额不足!', 302: '交易成功!',
                  400: '文件上传成功!', 401: '文件已存在!', 402: '文件已删除!'}
    path = setting.BASIS_DIR

    def __init__(self, conn):
        self.conn = conn

    # 功能分发
    def run(self):

        while True:
            try:
                obj = self.conn.recv(4)
                head_size = struct.unpack('i', obj)[0]  # 解析客户端发送的报头
                msg_dict = self.conn.recv(head_size)
                header_json = msg_dict.decode(setting.CODING)
                header_dict = json.loads(header_json)


                if hasattr(self, header_dict['cmd']):

                    game = getattr(self, header_dict['cmd'])
                    game(header_dict)

            except Exception:
                break
        self.conn.close()

    # 打包回复消息
    def send_respond(self, state_code, *args, **kwargs):
        send_data = kwargs
        send_data['state_code'] = state_code
        send_data['respond_msg'] = self.STATE_CODE[state_code]

        bytes_data = json.dumps(send_data).encode(setting.CODING)
        self.conn.send(bytes_data)

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
    def add_user(self, msg_dict):
        user_info = self.get_file()
        user_id = msg_dict['user_name']
        if user_id not in user_info.sections() and len(user_id) != 0:

            user_info.add_section(msg_dict['user_name'])
            user_info[user_id]['state'] = '0'
            user_info[user_id]['password'] = msg_dict['user_password']
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
            self.send_respond(state_code=200)

            log_msg = 'account:%s  operation:add_user  info:login successfully' % user_id
            loggers = Logger.logs('landing')
            loggers.info(log_msg)  # 记录日志

        else:
            self.send_respond(state_code=201)

    # 用户登录验证
    def login(self, msg_dict):
        user_info = self.get_file()     # 从数据库中获取用户信息
        user_id = msg_dict['user_id']
        send_msg = {}
        if msg_dict['user_id'] in user_info.sections():
            if user_info[user_id]['state'] == '0':
                if msg_dict['count'] < 3:
                    password = user_info[user_id]['password']
                    if msg_dict['user_password'] == password:
                        self.home_dir = r'%s\home\%s' % (
                            self.path, msg_dict['user_id'])  # 登录成功获取用户家目录
                        for k, v in user_info[user_id].items():
                            send_msg[k] = v
                        send_msg['user_id'] = user_id
                        self.send_respond(state_code=100, **send_msg)

                        log_msg = 'account:%s  operation:login  info:login successfully' % msg_dict[
                            'user_id']
                        loggers = Logger.logs('landing')
                        loggers.info(log_msg)  # 记录日志
                    else:
                        self.send_respond(state_code=101)
                else:
                    user_info[user_id]['state'] = '1'
                    user_info.write(
                        open(
                            r'%s\db\user_info.ini' %
                            self.path,
                            'w',
                            encoding=setting.CODING))  # 密码输出3次以上账号冻结
                    self.send_respond(state_code=102)

                    log_msg = 'account:%s  operation:login  info:account lockout' % msg_dict[
                        'user_id']
                    loggers = Logger.logs('landing')
                    loggers.info(log_msg)  # 记录日志

            else:
                self.send_respond(state_code=102)
        else:
            self.send_respond(state_code=101)

    # 修改密码
    def change_pwd(self, msg_dict):
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
    def recharge(self, msg_dict):
        user_info = self.get_file()
        user_id = msg_dict['user_id']
        send_msg = {}
        user_info[user_id]['balance'] = str(
            int(user_info[user_id]['balance']) + msg_dict['money'])
        user_info.write(
            open(
                r'%s\db\user_info.ini' %
                self.path,
                'w',
                encoding=setting.CODING))
        new_info = self.get_file()
        new_balance = new_info[user_id]['balance']
        send_msg['balance'] = new_balance
        self.send_respond(state_code=300, **send_msg)  # 充值成功返回一个成功状态给客户端

        log_msg = 'account:%s  operation:recharge  recharge_money:%s  info:recharge successfully' % \
                  (user_id, msg_dict['money'])
        loggers = Logger.logs('transaction')
        loggers.info(log_msg)  # 记录日志

    # 文件内存转换
    def bytes(self, bytes):
        if bytes < 1024:  # 比特
            bytes = str(round(bytes, 2)) + ' B'  # 字节
        elif 1024 <= bytes < 1024 * 1024:
            bytes = str(round(bytes / 1024, 2)) + ' KB'  # 千字节
        elif 1024 * 1024 <= bytes < 1024 * 1024 * 1024:
            bytes = str(round(bytes / 1024 / 1024, 2)) + ' MB'  # 兆字节
        else:
            bytes = str(round(bytes / 1024 / 1024 / 1024, 2)) + ' GB'  # 千兆字节

        return bytes

    # 内存转换
    def bytes_back(self, chars):
        ls = chars.split(' ')
        if ls[1] == 'B':
            length = float(ls[0])
        elif ls[1] == 'KB':
            length = float(ls[0]) * 1024
        elif ls[1] == 'MB':
            length = float(ls[0]) * 1024 * 1024
        else:
            length = float(ls[0]) * 1024 * 1024 * 1024

        return length

    # 个人空间使用大小
    def space_calculate(self):
        total_size = 0
        file_list = os.walk(self.home_dir, topdown=False)  # 获取指定目录下的文件夹列表
        for root, dirs, files in file_list:
            for name in files:
                file_size = os.path.getsize(os.path.join(
                    root, name))  # 将文件和所在文件夹名称拼接成文件路径并计算文件大小
                total_size = total_size + file_size
        total_size = self.bytes(total_size)

        return total_size

    # 购买存储空间
    def dilatation(self, msg_dict):
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
                'new_memory': str(new_memory) + 'GB',
                'new_balance': balance
            }
            self.send_respond(state_code=302, **send_msg)  # 充值成功返回客户端状态信息

            log_msg = 'account:%s  operation:dilatation  buy_spacey:%s  info:dilatation successfully' % \
                      (user_id, str(msg_dict['buy_memory']) + 'G')
            loggers = Logger.logs('transaction')
            loggers.info(log_msg)  # 记录日志

        else:
            send_msg = {
                'new_memory': user_info[user_id]['memory'],
                'new_balance': user_info[user_id]['balance']
            }
            self.send_respond(state_code=301, **send_msg)

    # 获取指定路径下文件列表
    def get_path(self, dir_path, root_dir, send_dict):

        file_list = os.listdir(dir_path)  # 获取客户端选择指定目录下的所有文件和文件夹
        send_dict['file_list'] = file_list
        self.conn.send(
            json.dumps(send_dict).encode(
                setting.CODING))  # 将获得的文件列表返回给客户端
        while True:
            recv = self.conn.recv(setting.Packet_Size)
            choice = json.loads(recv.decode(setting.CODING))
            if choice.isdigit():
                choice = int(choice)
                if choice < len(file_list):
                    file_path = os.path.join(
                        dir_path, file_list[choice])  # 将选择的文件和所在路径拼接
                    if os.path.isfile(
                            file_path):                         # 指定路径是文件则返回给客户端文件名
                        send_dict['file_path'] = file_path
                        send_dict['is_file'] = True
                        self.conn.send(
                            json.dumps(send_dict).encode(
                                setting.CODING))
                        return
                    elif os.path.isdir(file_path):    # 选择路径下是文件夹则进入文件夹
                        send_dict['file_path'] = file_path
                        return self.get_path(file_path, root_dir, send_dict)

                else:
                    return self.get_path(
                        dir_path, root_dir, send_dict)    # 选择不存在，返回当前文件夹
            elif choice == 'b' or choice == 'B':                                          # 返回上一级目录
                if dir_path == root_dir:                                 # 如果返回路径是个人家目录，则显示家目录
                    return self.get_path(dir_path, root_dir, send_dict)
                else:
                    file_path = os.path.dirname(
                        dir_path)                # 不是家目录则回退一级目录
                    return self.get_path(file_path, root_dir, send_dict)
            elif choice == 'q' or choice == 'Q':
                send_dict['end_flag'] = True
                self.conn.send(
                    json.dumps(send_dict).encode(
                        setting.CODING))    # 退出文件浏览
                return

    # 浏览文件，访问家目录
    def look_file(self, msg_dict):
        send_dict = {
            'end_flag': False,
            'is_file': False,
            'file_list': None,
            'file_path': None
        }
        self.get_path(self.home_dir, self.home_dir, send_dict)

    # 下载文件
    def download(self, msg_dict):
        user_id = msg_dict['user_id']

        if os.path.exists(msg_dict['server_file_path']):
            header_dict = {
                'state_code': 401,
                'respond_msg': self.STATE_CODE[401],
                'filename': msg_dict['server_file_path'],
                'md5': 'xxxx',
                'file_size': os.path.getsize(
                    r'%s' %
                    msg_dict['server_file_path'])}  # 制作报头
            header_json = json.dumps(header_dict)
            header_bytes = header_json.encode(setting.CODING)

            self.conn.send(struct.pack('i', len(header_bytes)))  # 发送报头长度
            self.conn.send(header_bytes)                         # 发送报头

            with open(r'%s' % msg_dict['server_file_path'], 'rb') as f:  # 发送下载文件内容
                f.seek(int(msg_dict['recv_size']))
                for line in f:
                    self.conn.send(line)

            log_msg = 'account:%s  operation:download  file_name:%s  info:download successfully' % \
                      (user_id, msg_dict['file_name'])
            loggers = Logger.logs('operation')
            loggers.info(log_msg)  # 记录日志
        else:
            header_dict = {
                'state_code': 402,
                'respond_msg': self.STATE_CODE[402],
                'filename': msg_dict['server_file_path'],
                'md5': 'xxxx',
                'file_size': os.path.getsize(
                    r'%s' %
                    msg_dict['server_file_path'])}  # 制作报头
            header_json = json.dumps(header_dict)
            header_bytes = header_json.encode(setting.CODING)

            self.conn.send(struct.pack('i', len(header_bytes)))  # 发送报头长度
            self.conn.send(header_bytes)  # 发送报头

    # 上传文件
    def uploading(self, msg_dict):

        user_info = self.get_file()
        user_id = msg_dict['user_id']
        total_size = int(user_info[user_id]['memory'].split('G')[0])
        total_v = total_size * 1024 * 1024 * 1024
        file_name = os.path.split(msg_dict['file_path'])[1]
        use_space = int(self.bytes_back(user_info[user_id]['use_space']))
        send_msg = {
            'flag': True,
            'use_space': None,
            'surplus_space': None,
            'file_size': self.bytes(msg_dict['file_size'])
        }      # 发送给客户端的状态信息
        if use_space + msg_dict['file_size'] <= total_v:  # 判断文件大小是否超过内存
            use_space += msg_dict['file_size']
            user_info[user_id]['use_space'] = self.bytes(use_space)
            user_info.write(
                open(
                    r'%s\db\user_info.ini' %
                    self.path,
                    'w',
                    encoding=setting.CODING))
            send_msg['use_space'] = self.bytes(use_space)
            uploading_path = r'%s\home\%s\share\%s' % (
                setting.BASIS_DIR, user_id, file_name)
            self.conn.send(json.dumps(send_msg).encode(setting.CODING))
            with open(uploading_path, 'wb') as f:
                recv_size = 0
                while recv_size < msg_dict['file_size']:
                    line = self.conn.recv(1024)
                    f.write(line)
                    recv_size += len(line)

            log_msg = 'account:%s  operation:uploading  file_name:%s  info:uploading successfully' % \
                      (user_id, file_name)
            loggers = Logger.logs('operation')
            loggers.info(log_msg)  # 记录日志

        else:
            surplus_space = total_v - int(user_info[user_id]['use_space'])
            send_msg['flag'] = False
            send_msg['surplus_space'] = self.bytes(surplus_space)
            self.conn.send(json.dumps(send_msg).encode(setting.CODING))

    # 删除文件
    def del_file(self, msg_dict):

        back_msg = {}
        users_info = self.get_file()
        del_path = msg_dict['file_path']
        file_size = os.path.getsize(del_path)
        os.remove(r'{}'.format(del_path))
        use_memory = self.space_calculate()
        users_info[msg_dict['user_id']]['use_space'] = use_memory
        users_info.write(
            open(
                r'%s\db\user_info.ini' %
                self.path,
                'w',
                encoding=setting.CODING))
        file_name = os.path.split(del_path)[1]
        back_msg['file_size'] = self.bytes(file_size)
        back_msg['file_name'] = file_name
        self.send_respond(state_code=402, **back_msg)

        log_msg = 'account:%s  operation:del file  file_name:%s  info:del file successfully' % (
            msg_dict['user_id'], file_name)
        loggers = Logger.logs('operation')
        loggers.info(log_msg)  # 记录日志


def main():

    thread_pool = threadpool.ThreadPoolManger(setting.Max_Number)
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8070))
    server.listen(5)
    print("服务端已开启，等待用户连接...")

    while True:
        conn, client_addr = server.accept()
        client = Service(conn)
        thread_pool.add_job(client.run,)
        print('from servers ', client_addr)

    server.close()
