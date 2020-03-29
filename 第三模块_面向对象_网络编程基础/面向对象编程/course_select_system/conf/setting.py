# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0:11
# @Author  : XiaTian
# @File    : setting.py

import os
import logging

FILE_PATH = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))      # 获取程序存储根目录

# 设置日志的级别
LOG_LEVEL = logging.INFO

LOG_TYPE = {
    'manager': 'manager.log',                                         # 获取日志类型及日志文件名
    'teacher': 'teacher.log',
    'student': 'student.log'
}
