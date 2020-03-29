# -*- coding: utf-8 -*-
# @Time    : 2020/1/15  14:45
# @Author  : XiaTian
# @File    : 7_二叉树.py


class BigTree:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BigTree('A')
b = BigTree('B')
c = BigTree('C')
d = BigTree('D')
e = BigTree('E')
f = BigTree('F')
g = BigTree('G')

root = e
e.lchild = a
e.rchild = g
a.rchild = c
g.rchild = f
c.lchild = b
c.rchild = d

# print(a.rchild.rchild.data)


# 二叉树前序遍历：一条分支找到底，再找下一条分支
def pre_order(root):
    if root:
        print(root.data, end=', ')
        pre_order(root.lchild)
        pre_order(root.rchild)


# 二叉树的中序遍历：
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=', ')
        in_order(root.rchild)


# 二叉树后序遍历：从后向前遍历，遇到根后停止，机修找吓一跳分支，最后找根
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=', ')


# 二叉树层级遍历：利用队列，每找完一层，对应层的元素出队，下一次能元素入队
from collections import deque


def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.data, end=', ')
        if node.lchild:
            q.append(node.lchild)
        if node.rchild:
            q.append(node.rchild)

level_order(root)
























