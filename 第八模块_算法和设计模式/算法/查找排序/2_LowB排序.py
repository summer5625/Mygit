# -*- coding: utf-8 -*-
# @Time    : 2020/1/3  15:34
# @Author  : XiaTian
# @File    : 2_LowB排序.py
import random


# 冒泡排序
def bubble_sort(li):

    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 -i):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return


# 选择排序
def select_sort(li):

    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]
        print(li)


# li = [3, 5, 2, 4, 8 ,6, 9, 1,7]
# print(li)
# bubble_sort(li)
# select_sort(li)


# 插入排序
def insert_sort(li):

    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1

        li[j+1] = tmp
    print(li)


li = [2, 5, 8, 4, 6, 9, 7, 1, 3]
# insert_sort(li)

















