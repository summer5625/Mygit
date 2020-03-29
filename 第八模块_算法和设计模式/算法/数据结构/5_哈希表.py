# -*- coding: utf-8 -*-
# @Time    : 2020/1/14  16:57
# @Author  : XiaTian
# @File    : 5_哈希表.py


class LinkList:

    class Node:

        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:

        def __init__(self, node):

            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):

        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ", ".join(map(str, self)) + ">>"


class HashTable:

    def __init__(self, size=101):
        self.size = size  # 哈希表长度
        self.T = [LinkList() for i in range(self.size)]

    # 哈希表和全域的映射关系
    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print('插入值重复')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


ht = HashTable()
ht.insert(1)
ht.insert(2)
ht.insert(102)
print(', '.join(map(str, ht.T)))
print(ht.find(102))

















































