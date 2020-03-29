# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  13:30
# @Author  : XiaTian
# @File    : subscriber.py

# 创建订阅者

import redis

conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

# 创建订阅者对象

# 1、生成一个订阅者对象
pubsub = conn.pubsub()

# 2、订阅一个消息
pubsub.subscribe("summer")

# 3、接收发布的订阅消息
while True:
    print('working....')
    msg = pubsub.parse_response()
    print(msg)















