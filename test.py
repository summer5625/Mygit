# -*- coding: utf-8 -*-
# @Time    : 2019/5/12  20:21
# @Author  : XiaTian
# @File    : test.py


# from socket import *
#
# sever = socket(AF_INET, SOCK_STREAM)
# sever.bind(('127.0.0.1',8070))
# sever.listen(5)
# while True:
#     conn, addr = sever.accept()
#     data = conn.recv(1024)
#     print(data.decode('utf-8'))
#     # conn.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n', 'utf-8'))
#     conn.sendall(bytes('<h1>Hello World</h1>', 'utf-8'))
#     conn.close()
#
# sever.close()


# v = 30
# print(hex(v))
# print(bin(v))
#
# # a = oct(30)
# # print(int(a, 8))
#
# c = '0b1010'
# print(int(c, 2))
#
# a = '0o123'
# print(int(a, 8))
#
# d = '0x1a2'
# print(int(d, 16))


# print(0 or False and 4)

# a = range(0, 9)
# print(a)
# for i in a:
#     print(i)


# a = '*wor*od* '
#
# '增删改查'
# print(a)
# print(a.find('b')) # 查找字符，找到返回1，找不到返回-1
# print(a.strip()) # 移除空白
# print(a.lstrip()) # 移除前面空白
# print(a.rstrip()) # 移除后面空白
#
# print(len(a)) # 看长度
# print(a.count('o')) # 统计字符出现次数
# print(a.replace('*', 'd'))  # 替换指定字符
# print(a.index('w')) # 查找字符的位置
# print(a[1:6:2])  #最后面一个数代表每隔几个字符取一次

# 列表
# a = ['a', 'b', 1, 5 ,'rdsf', '9', 8]
# a.append('5') # 追加元素到最后面
# a.remove('5') # 删除，无返回值
# b = a.pop(1) # 删除，返回删除的元素，里面数值代表列表元素的索引，不是元素
# del a[0]  # 删除
# print(a)


# 元组,只能看，无法改
# a = ('a', 'b', 1, 5 ,'rdsf', '9', 8)
#
# print(a[1])

# 字典
# a = {'a': 2, 'b':[1,2,3], 'c': 'word'}
# print(a['a']) # 查看
# a['e'] = 123
# print(a)  # 添加
#
# b = a.fromkeys(['g', 2],3)
# print(b)


# def hand():
#
#     print(123)
#
#     def inner():
#         print(45)
#
#         return '停止吧'
#
#     print(789)
#
# hand()


class Person:
    def __enter__(self):
        print("我是enter")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("我是exit ")
    def __call__(self, *args, **kwargs):
        print("我是call")
p = Person()
p()
with p: # 自动调用__enter__
    print("哈哈哈")

























