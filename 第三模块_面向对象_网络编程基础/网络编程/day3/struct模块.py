# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 0:37
# @Author  : XiaTian
# @File    : struct模块.py

import struct

a = struct.pack('i',125000006)   # i代表整型，l代表长整型 ，讲数字转换成固定长度的二进制
print(a)
b = struct.unpack('i',a)    # 解析出来是个元组(1256,)
print(b)