# -*- coding: utf-8 -*-
# @Time    : 2019/11/8  23:20
# @Author  : XiaTian
# @File    : md5.py

import hashlib


def get_md5(origin):
    '''
    密码加密
    :param origin:
    :return:
    '''

    ha = hashlib.md5()
    ha.update(origin.encode('utf-8'))

    return ha.hexdigest()