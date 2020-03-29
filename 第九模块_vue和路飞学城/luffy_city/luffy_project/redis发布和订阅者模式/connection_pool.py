# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  13:21
# @Author  : XiaTian
# @File    : connection_pool.py

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True, max_connections=10)

conn = redis.Redis(connection_pool=pool)

ret = conn.get('n1')
print(ret)