# -*- coding: utf-8 -*-
# @Time    : 2020/1/13  14:26
# @Author  : XiaTian
# @File    : 5_排序练习.py
'''
给两个字符串s和t，判断t是否为s的重新排列后组成的单词
思路：
    将原字符串拆分成列表，然后对两个新列表分别进行快速排序，排序后分别将两个列表合并成一个字符串，比较两个字符串是否一致
'''


def partition(li, left, right):
    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
    return li


def sort_letter(st):
    li = list(st)
    s = quick_sort(li, 0, len(li) - 1)
    return s


def compare(s, t):
    ls = len(s)
    lt = len(t)
    if ls != lt:
        return 'False'

    sl = sort_letter(s)
    tl = sort_letter(t)

    if ''.join(sl) == ''.join(tl):
        return 'True'
    else:
        return 'False'


s = 'anagraml'
t = 'najaram'
# a = compare(s, t)


'''

给定一个m*n的二维列表，查找一个数是否存在：每一行列表从左到右已经拍好序了，每一行第一个数都比上一行最后一个数大
思路：
    先合并成一个列表，用二分查找，找到在新列表中位置，在计算出在原二维列表位置
    
注：合并后列表是有序列表
'''


def search(li, val):
    m = len(li)  # 二维数组的行数
    n = len(li[0])  # 二维数组的列数

    new_li = []
    for i in li:
        new_li.extend(i)
    left = 0
    right = len(new_li) - 1
    while left <= right:
        mid = (left + right) // 2
        if new_li[mid] < val:
            left = mid + 1
        elif new_li[mid] > val:
            right = mid - 1
        elif new_li[mid] == val:
            row = mid // m
            column = mid % m
            return (row, column)
    else:
        return None


li = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
# v = search(li, 25)
# print(v)
#
# print(li[4][4])


'''

给定一个列表和一个整数，设计算法找出两个数的下标，使得两个数之和为给定的整数。保证仅有一个结果
思路：
   先对最开始列表排序，在错位相加，求出所有可能存在的和，组成新的二维列表列表，新列表也是有序的
    
'''

def find(li, val):

    new_li = []
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            new_li.append([li[i] + li[j], i, j])
    print(new_li)

    left = 0
    right = len(new_li) - 1
    while left <= right:
        mid = (left + right) // 2
        if new_li[mid][0] < val:
            left = mid + 1
        elif new_li[mid][0] > val:
            right = mid - 1
        elif new_li[mid][0] == val:

            return sorted([new_li[mid][1], new_li[mid][2]])
    else:
        return None


a = [1,2,4,5,9]
b = find(a, 7)
print(b)

























