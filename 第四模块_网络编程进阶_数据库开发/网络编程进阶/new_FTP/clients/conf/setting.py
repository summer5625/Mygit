# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0:17
# @Author  : XiaTian
# @File    : setting.py

import os
import logging


BASIS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 获取程序所在的路径

LOG_LEVEL = logging.INFO                                                  # 设定日志级别

LOG_TYPE = {                                                              # 日志类型
                'landing':'landing.log',
                'operation':'operation.log',
                'transaction':'transaction.log'
            }

IP = ('127.0.0.1',8070)  # 服务器ip和端口

CODING = 'utf-8'         # 字符编码格式

Share_Path = r'%s\file_path'%BASIS_DIR                                    # 用户上传文件存储路径

Packet_Size = 8192                                                        # 最大传送长度

Request_Queue_Size = 5                                                    # 最大等待连接数

HEAD_DICT = {
                'cmd':None,
                'md5':None,
                'file_name':None,
                'file_size':None
            }
# 获取每个用户的家目录
class Home_Dir:

    def __init__(self,name):
        self.name = name

    def __str__(self):

        return r'%s\service\file_path\%s'%(BASIS_DIR,self.name)









