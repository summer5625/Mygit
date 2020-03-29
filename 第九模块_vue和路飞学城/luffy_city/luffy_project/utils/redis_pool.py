# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  14:59
# @Author  : XiaTian
# @File    : redis_pool.py
import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True, max_connections=10)

conn = redis.Redis(connection_pool=POOL)