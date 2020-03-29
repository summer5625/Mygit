# -*- coding: utf-8 -*-
# @Time    : 2019/12/12  14:14
# @Author  : XiaTian
# @File    : book.py


def transform(str):
    count = str.count('.')

    if count != 3:
        return 'ip不合法!'

    str_list = str.split('.')
    bin_list = []
    for i in str_list:

        binary = bin(int(i))
        binary = binary.split('b')[-1]

        if len(binary) < 8:

            long = '0' * (8 - len(binary)) + binary

        else:
            long = binary

        bin_list.append(long)

    long_bin = ''.join(bin_list)

    return int(long_bin, 2)


# a = lambda x, y: x*y if x <y else x+y

# print(a(3, 5))
# print(list(map(lambda x: x+5, range(5))))

#
# def func(**kwargs):
#
#     print(kwargs)


# a = 1
# b = 1
#
# print(a is b)

# a = [1, 2, 3, 5]
# b = [1, 2, 3, 5]


# print(id(a))
# print(id(b))

# a.append([6, 5])

# b = a.copy()
# a[1] = 'v'
# print(a)
# print(b)

# a = dict.fromkeys(['key1', 'key2'], [])

# a['key1'].append(666)
# print(a)

# a['key1'] = 777
# print(a)


def num():
    return [lambda x: i * x for i in range(4)]


# print([m(2) for m in num()])

# a = num()
# print(a)
# print(a[0](1))


# dd = '1 + 2 + 3'

# print(eval(dd))
# print(exec(dd))
# print(type(dd))
#
# print(hash(dd))

# x = 3/3

# print(round(x, 3))
# print(divmod(6, 5))
#
# print(pow(2, 3))
#
# print(sum([1, 2, 3]))

for i in range(1, 10):

    li = []
    for j in range(1, i + 1):
        s = '%s * %s = %s' % (i, j, i * j)
        li.append(s)
    # print('  '.join(li))

# m = '\n'.join(['  '.join([ '%s * %s = %s' % (i, j ,i*j) for j in range(1, i+1)]) for i in range(1, 10)])

import time

# print(time.time())
# print(time.localtime())
# print(time.gmtime())

# y = time.localtime()

# print('%s-%s-%s' % (y.tm_year, y.tm_mon, y.tm_mday))
# print(time.mktime(y))
# print(time.strftime('%Y-%m-%d %H:%M:%S', y))


import datetime

# a = datetime.datetime.now()
# print(a)
#
# b = a + datetime.timedelta(minutes=10)
#
# print(b)

import random

# a = random.randint(1, 10)
# print(a)

# b = random.randrange(20)
# print(b)

# c = random.choice('kkkjhubgfvc')
# print(c)

# s = random.sample(1, 20)
# print(s)

# l = list(range(20))

# random.shuffle(l)
# print(l)

import hashlib

# m = hashlib.md5()
# m.update(b'562')
# print(m.hexdigest())


import re

# tt = "Tina is a good girl, she is cool, clever, and so on..."
# rr = re.compile(r'\w*oo\w*')
# print(rr.findall(tt))
# p = re.compile(r'ab.*c')
# s = 'abcaxc'
# print(p.match(s).group())
# p_f = re.compile(r'ab.*?c')
# print(p_f.match(s).group())


# print(re.match('com', 'kkcomwww.runcomoob'))
# print(re.search('com', 'comwww.runcomoob'))

# import logging
#
#
# logger = logging.getLogger('web')
#
# logger.setLevel(logging.DEBUG)
#
# ch = logging.StreamHandler()
# fh = logging.FileHandler('ff.log')
#
# ch.setLevel(logging.INFO)
# fh.setLevel(logging.DEBUG)
#
# logger.addHandler(ch)
# logger.addHandler(fh)
#
# console_formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')
# ch.setFormatter(console_formatter)
# fh.setFormatter(console_formatter)
#
# logger.info('i love you')

h = (i % 2 for i in range(10))


# print(h.__next__())

# print(1 < 2 == 2)


# def func(a, b=[]):
#
#     print(a)
#     print('b', type(b))


# s = '1,2,3'
#
# a = s.split(',')
# print(a)

# a = [1,4,9,16,25,36,49,36,81,100]
#
# b = {}
#
# b = b.fromkeys(a)
# c = list(b.keys())


class Stack:

    def __init__(self):

        self.stack = []

    def push(self, value):

        self.stack.append(value)

    def pop(self):

        if self.stack:
            self.stack.pop()
        else:
            raise LookupError('stack is empty!')

    def is_empty(self):

        return bool(self.stack)

    def top(self):

        return self.stack[-1]


# a = Stack()
# a.push(2)
# print(a.top())

# a = ['s', 'n']
#
# a = ''.join(a)
# print(a)
#
# b = '{}ghgh{}'.format(1,2)
# print(b)
#
# c = f'ffff plus {3+5}'
# print(c)

# from string import Template
#
# t = Template('Hello $name!')
# t.substitute(name='summer')
# print(t)


def bid(max):
    n = 0
    a = 0
    b = 1

    while n < max:
        yield b
        c = a + b
        a = b
        b = c
    return


# f = bid(6)


# print(f)
# print(next(f))


# def fiv():
#     print('ok1')
#     x = 10
#     print(x)
#     x = yield 3
#     print(x)
#     yield 5
#
#
# b = fiv()
# print(next(b))
#
# c = b.send(66)
# print(c)


def look(data, n):
    mid = int(len(data) / 2)

    if mid > 0:
        if data[mid] == n:

            print('找到了，索引为%s' % list(range(20)).index(n))

        elif data[mid] > n:

            print('没找到，中数%s比查找值%s大' % (data[mid], n))

            look(data[:mid], n)
        else:
            print('没找到，中数%s比查找值%s小' % (data[mid], n))

            look(data[mid:], n)


import random


# p = random.randint(1,20)
# v = random.choice('fdcvbghu')


# class Foo:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         print('from func')
#
#     def __getitem__(self, item):
#         print('getattr><')
#
#         return self.__dict__[item]  # 当输入的不是字典中的key时会报错
#         # return self.__dict__.get(item)    # 当输入的不是字典中的key时不会报错
#
#     def __setitem__(self, key, value):
#
#         print('setattr><', key, value)
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         print('delitem><')
#         # del self.__dict__[key]
#         self.__dict__.pop(key)
#
#
# f = Foo('alex', 89)
# f['sex'] = 'nv'
# print(f['name'])


class Foo:

    b= None
    s = None

    def __init__(self, m, n):

        self.m = int(m)
        self.n = int(n)
        self.compare()

    def compare(self):

        if self.n - self.m < 0:

            self.b = self.m
            self.s = self.n
        else:
            self.b = self.n
            self.s = self.m

    def cal(self):

        b = 1
        s = 1
        b_s = 1

        for i in range(1, self.b+1):
            b *= i

        for j in range(1, self.s+1):

            s *= j

        if self.b - self.s == 0:
            b_s = 1
        else:
            for x in range(1, self.b - self.s + 1):
                b_s *= x

        result = b / (s * b_s)

        return result














