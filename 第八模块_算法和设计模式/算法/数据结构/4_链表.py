# -*- coding: utf-8 -*-
# @Time    : 2020/1/14  16:03
# @Author  : XiaTian
# @File    : 4_链表.py


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


# 使用头插法创造链表
def create_linklist(li):

    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


# 使用尾插法创建链表
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk = create_linklist_tail([1,2,3,4,5])
print_linklist(lk)












