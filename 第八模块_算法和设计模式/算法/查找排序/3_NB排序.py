# -*- coding: utf-8 -*-
# @Time    : 2020/1/11  14:05
# @Author  : XiaTian
# @File    : 3_NB排序.py


# 快速排序，时间复杂度O(nlogn)
# 坏处：使用递归很消耗内存资源，当给出一个倒序列表时排序的时间复杂度会变n的平方，解决办法在排序前将列表第一个元素随机替换成列表中的任意一个数
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


def quick_sort(data, left, right):

    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)
    print(data)


# li = [2, 6, 4, 1, 8, 7, 3, 9, 5]
# quick_sort(li, 0, len(li)-1)


# 堆排序
def sift(li, low, high):
    '''

    :param li: 乱序列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素位置
    :return:
    '''
    i = low # 根节点序号
    j = 2 * i + 1 # 左子节点序号
    tmp = li[low]
    while j <= high: # 子节点不超过列表长度
        if j + 1 <= high and li[j+1] > li[j]: # 右节点存在且有节点大于左节点
            j = j + 1 # 转换到有节点查询
        if li[j] > tmp: # 子节点大于根节点
            li[i] = li[j] # 交换位置
            i = j # 向下走一层
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    # 建堆
    for i in range((n-2)//2, -1, -1): # 代表从后向前数数
        sift(li, i, n-1)
    print(li)
    # 交换父子节点位置
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)
    print(li)


li = [2, 6, 4, 1, 8, 7, 3, 9, 5]
# heap_sort(li)


# import heapq  # 导入堆排序内置模块
#
#
# heapq.heapify(li) # 建堆
# n = len(li)
# print(li)
# for i in range(n):
#     print(heapq.heappop(li), end=',')  # heappop(li)每次吐出一个元素
# 找出前n个大的数


def new_sift(li, low, high):
    '''

    :param li: 乱序列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素位置
    :return:
    '''
    i = low # 根节点序号
    j = 2 * i + 1 # 左子节点序号
    tmp = li[low]
    while j <= high: # 子节点不超过列表长度
        if j + 1 <= high and li[j+1] < li[j]: # 右节点存在且有节点小于左节点
            j = j + 1 # 转换到有节点查询
        if li[j] < tmp: # 子节点小于根节点
            li[i] = li[j] # 交换位置
            i = j # 向下走一层
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    n = len(heap)
    for i in range((n-2)//2, -1, -1):
        new_sift(heap, i, n-1)
    for i in range(n, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            new_sift(heap, 0, k-1)
    print(heap)

    for i in range(n-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        new_sift(heap, 0, i-1)

    return heap


a = topk(li, 9)
print(a)


#  归并排序：将两个有序列表合并成一个有序列表
def merge(li, low, mid, high):

    tmp = []
    i = low
    j = mid + 1
    while i <= mid and j<=high:
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1

    li[low:high+1] = tmp
    print('merge:', tmp)


def merge_sort(li, low, high):

    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        print('sort:', li[low:high])
        merge(li, low, mid, high)


# merge_sort(li, 0, len(li)-1)
# print(li)




































