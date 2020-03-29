# -*- coding: utf-8 -*-
# @Time    : 2019/7/2  23:37
# @Author  : XiaTian
# @File    : servr.py

from socket import *
import struct
import os
import configparser
import json
from threading import currentThread

import new_pool


class Service:

    STATE_CODE = {100:'登录成功!', 101:'账号或者密码错误',102:'账号被冻结',
                  201:'账号已存在!', 200:'注册成功!',
                  300:'充值成功!', 301:'余额不足!', 302:'交易成功!',
                  400:'文件传输完成!', 401:'文件已存在!', }
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, conn):
        # self.server = socket(AF_INET, SOCK_STREAM)
        # self.server.bind(('127.0.0.1', 8070))
        # self.server.listen(5)
        self.conn = conn
        # print("服务端已开启，等待用户连接...")

    # 功能分发
    def run(self):
        # self.conn = conn

        while True:
            try:
                print('thread %s is running run' % currentThread().getName())
                obj = self.conn.recv(4)
                head_size = struct.unpack('i', obj)[0]  # 解析客户端发送的报头
                print(self.conn)
                msg_dict = self.conn.recv(head_size)
                print(msg_dict)
                header_json = msg_dict.decode('utf-8')
                header_dict = json.loads(header_json)

                if hasattr(self, header_dict['cmd']):

                    game = getattr(self, header_dict['cmd'])
                    game(header_dict)

            except Exception:
                break
        # self.conn.close()

    # 打包回复消息
    def send_respond(self, state_code,*args,**kwargs):
        print('thread %s is running send_respond' % currentThread().getName())
        send_data = kwargs
        send_data['state_code'] = state_code
        send_data['respond_msg'] = self.STATE_CODE[state_code]

        bytes_data = json.dumps(send_data).encode('utf-8')
        self.conn.send(bytes_data)

    # 获取用户信息
    def get_file(self):
        print('thread %s is running get_file' % currentThread().getName())
        file_path = r'%s\user_info.ini' % self.path      # 获取打开文件的路径
        if os.path.exists(file_path):
            conf = configparser.ConfigParser()
            conf.read(file_path, encoding='utf-8')
        else:
            with open(file_path, 'w') as f:
                f.write('')
                f.close()
            conf = configparser.ConfigParser()
            conf.read(file_path, encoding='utf-8')

        return conf                                          # 返回文件内容

    # 用户登录验证
    def login(self, msg_dict):
        print('thread %s is running login' % currentThread().getName())
        user_info = self.get_file()     # 从数据库中获取用户信息
        user_id = msg_dict['user_id']
        if msg_dict['user_id'] in user_info.sections():
            if user_info[user_id]['state'] !=0:
                if msg_dict['count'] < 3:
                    password = user_info[user_id]['password']
                    if msg_dict['user_password'] == password:
                        self.home_dir = r'%s\home\%s' % (self.path, msg_dict['user_id'])  # 登录成功获取用户家目录
                        self.send_respond(state_code=100)

                    else:
                        self.send_respond(state_code=101)
                else:
                    user_info[user_id]['state'] = '1'
                    user_info.write(
                        open(
                            r'%s\user_info.ini' %
                            self.path,
                            'w',
                            encoding='utf-8'))  # 密码输出3次以上账号冻结
                    self.send_respond(state_code=102)


            else:
                self.send_respond(state_code = 102)
        else:
            self.send_respond(state_code=101)


def main():

    thread_pool = new_pool.ThreadPoolManger(5)
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8070))
    server.listen(5)
    print("服务端已开启，等待用户连接...")

    while True:
        conn, client_addr = server.accept()
        client = Service(conn)
        thread_pool.add_job(client.run,)
        print('from servers ', client_addr)
        print('thread %s is running ' % currentThread().getName())

    # client.server.close()


main()