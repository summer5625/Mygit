# -*- coding: utf-8 -*-
# @Time    : 2020/1/17  16:36
# @Author  : XiaTian
# @File    : 11_动态规划_钢条切割.py
'''

钢条出售价格和长度关系：

长度i：  1    2    3    4    5    6    7    8    9    10

价格p：  1    5    8    9    10   17   17   20   24   30

问题：
    有一段长度为n的钢条，求切割钢条方案，使收益最大

'''
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


# #################################自顶向下切割
def cut_rod_recur_1(p, n):

    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recur_1(p, i) + cut_rod_recur_1(p, n-i))
        return res


def cut_rod_recur_2(p, n):

    if n == 0:
        return 0

    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i]+cut_rod_recur_2(p, n-i))

    return res


# #################################自下向上切割
def cut_rod_dp(p, n):

    res = [0]
    for i in range(1, n+1):
        r = 0
        for j in range(1, i+1):
            r = max(r, p[j]+res[i-j])
        res.append(r)

    return res[n]


# #################################输出最优解
def cut_rod_solution(p, n):
    res_r = [0]
    res_s = [0]
    a = n
    for i in range(1, n + 1):
        r = 0
        s = 0
        for j in range(1, i + 1):
            if p[j] + res_r[i - j] > r:
                r = p[j] + res_r[i - j]
                s = j
        res_r.append(r)
        res_s.append(s)

    solution = []
    while n > 0:
        solution.append(res_s[n])
        n -= res_s[n]
    return res_r[a], solution


a = cut_rod_solution(p, 20)
print(a)








