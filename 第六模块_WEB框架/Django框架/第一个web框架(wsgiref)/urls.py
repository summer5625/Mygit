# -*- coding: utf-8 -*-
# @Time    : 2019/9/25  10:37
# @Author  : XiaTian
# @File    : urls.py

from views import *

url_patterns = [
    ('/index',index),
    ('/login',login),
    ('/favicon.ico',favicon),
    ('/auth',auth)
]