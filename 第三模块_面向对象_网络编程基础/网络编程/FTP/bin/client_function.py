# -*- coding: utf-8 -*-
# @Time    : 2019/5/6  1:16
# @Author  : XiaTian
# @File    : client_run.py

import os
import sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)


from client import client

if __name__ == '__main__':
    client.main()