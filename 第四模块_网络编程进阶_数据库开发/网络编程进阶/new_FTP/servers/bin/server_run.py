# -*- coding: utf-8 -*-
# @Time    : 2019/5/6  1:17
# @Author  : XiaTian
# @File    : server_run.py

import os
import sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)

from core import server

if __name__ == '__main__':
    server.main()