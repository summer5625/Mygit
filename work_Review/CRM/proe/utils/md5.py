# -*- coding: utf-8 -*-
# @Time    : 2020/2/13  12:53
# @Author  : XiaTian
# @File    : md5.py
import hashlib


def get_md5(origin):

    ha = hashlib.md5()
    ha.update(origin.encode('utf-8'))
    return ha.hexdigest()