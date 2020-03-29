# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  13:28
# @Author  : XiaTian
# @File    : release.py

# 创建发布者,相当于一个广播，当改变某个数据时，收听这个广播的所有对应的数据对象都会发生改变

import redis

conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

# 创建发布者
conn.publish('summer', 'You have a lot of good man card')

