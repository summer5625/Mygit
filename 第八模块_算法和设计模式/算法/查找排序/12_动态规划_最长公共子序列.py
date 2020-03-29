# -*- coding: utf-8 -*-
# @Time    : 2020/1/18  13:56
# @Author  : XiaTian
# @File    : 12_动态规划_最长公共子序列.py
'''

问题：给定两个序列列X和Y，求X和Y⻓长度最⼤大的公共⼦子
序列列。例：X="ABBCBDE" Y="DBBCDB" LCS(X,Y)="BBCD"

'''
def lcs_length(x, y):

    m = len(x)
    n = len(y)
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


# a = lcs_length('ABCBDAB', 'BDCABA')
# print(a)
def lcs(x, y):

    m = len(x)
    n = len(y)
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    b = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] > c[i][j-1]: # 来自上方
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:  # 来自左方
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    return c[m][n], b


def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))


a = lcs_trackback('ABCBDAB', 'BDCABA')
print(a)
























