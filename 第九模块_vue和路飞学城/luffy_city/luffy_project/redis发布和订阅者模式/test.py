# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  13:18
# @Author  : XiaTian
# @File    : test.py

import redis

# decode_responses=True从redis里面来的数据不再是byte类型，而是字符串
conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

conn.set("n1", "v1")

conn.hset("n2", "key2", "v2")
conn.hset("n2", "key3", "v3")

"""
hset相当于存放结构：{n2: {key2: v2}}
redis里面所有的数据存放类型只支持一层字典，要想存放层字典需要转换成字符串

"""

ret1 = conn.get("n1")
ret2 = conn.hget("n2", "key2")  # 一次只能存一条数据
ret3 = conn.hget("n2", "key3")  # 一次只能存一条数据
ret4 = conn.hgetall("n2")  # 取出对应的所有数据

# print(ret1)
# print(ret2)
# print(ret3)
# print(ret4)

conn.hmset('n3', {"key4": "v4", "key5": "v5"})  # 可以批量添加数据
ret5 = conn.hgetall('n3')
# print(ret5)

# conn.delete('SETTLEMENT_1_1')
# conn.delete("SETTLEMENT_1_2")
print(conn.hgetall('SETTLEMENT_1_1'))

a = {
    'course_coupon_dict': '{"1": {"id": 1, "name": "双十一大活动", "coupon_type": "通用券", "object_id": 1, "money_equivalent_value": 20, "off_percent": 0, "minimum_consume": 0}, "2": {"id": 2, "name": "双十一满减优惠", "coupon_type": "满减券", "object_id": 1, "money_equivalent_value": 30, "off_percent": 0, "minimum_consume": 100}}',
    'course_img': 'course/2019-11/python.jpg',
    'default_course_coupon_id': '1',
    'id': '1',
    'title': 'Python21天入门',
    'price': '30.0',
    'valid_period': '30'
}
