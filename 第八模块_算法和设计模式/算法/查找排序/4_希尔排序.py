# -*- coding: utf-8 -*-
# @Time    : 2020/1/12  17:12
# @Author  : XiaTian
# @File    : 4_希尔排序.py
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d = d // 2


import random
#
# li = list(range(100))
# random.shuffle(li)
# shell_sort(li)
# print(li)


# 计数排序：生成一个与要排序列表长度相同的连续列表，统计要排序列表中相同元素出现的次数并存到连续的列表中
def count_sort(li, max_count):
    count = [0 for i in range(max_count+1)]
    for i in li:
        count[i] += 1

    li.clear()
    for ind, val in enumerate(count):
        for j in range(val):
            li.append(ind)
    print(li)


li = [random.randint(0, 100) for i in range(100)]
# count_sort(li, 15)


# 桶排序：将数据分为多段，分别对每一段进行排序，然后在合并（分段照计数排序方法进行连续数据分段）
def bucket_sort(li, n, max_num):

    buckets = [[] for i in range(n)]
    for val in li:
        i = min(val // (max_num // n), n-1)  # 放到几号桶
        buckets[i].append(val)

        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for i in buckets:
        sorted_li.extend(i)
    return sorted_li

# print(li)
# a = bucket_sort(li, 3, 15)
# print(a)


# 基数排序：在桶排序的基础上将数分为不同位数，将每位分别进行排序
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:

        buckets = [[] for i in range(10)]
        for var in li:
            digit = (var // (10 ** it )) % 10
            buckets[digit].append(var)
        # print(buckets)
        li.clear()
        for i in buckets:
            li.extend(i)
        it += 1
    return li


a = radix_sort(li)
print(a)











