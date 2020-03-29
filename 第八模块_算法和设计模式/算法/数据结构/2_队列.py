# -*- coding: utf-8 -*-
# @Time    : 2020/1/14  13:15
# @Author  : XiaTian
# @File    : 2_队列.py


class Queue:

    def __init__(self, size=100):
        self.size = size
        self.rear = 0 # 队尾指针
        self.front = 0 # 队首指针
        self.queue = [0 for i in range(size)]

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size  # 进队列队尾指针加1
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size # 删除数据时队首指针加1
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty.')

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# q = Queue(5)
# for i in range(4):
#     q.push(i)

# print(q.is_filled())
# print(q.pop())

# ######队列内置模块, deque是双向队列，使用deque创建的对列，当队列满时，向里面再插入数据是不会报错的，队列会先将最先进去的元素删除，然后在插入新数据
from collections import deque


# q = deque()

# 用于单向队列
# q.append(6) # 队尾进
# print(q.popleft()) # 队首出

# 用于双向队列
# q.appendleft(3) # 队首进
# print(q.pop()) # 队尾出


def tail(n):
    with open('test.text', 'r') as f:
        q = deque(f, n) # f表示新建队列时向队列里面添加的元素，格式是列表格式，n表示队列的长度
        print(q)
        return q

for lin in tail(5):
    print(lin, end='')











