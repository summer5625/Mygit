# -*- coding: utf-8 -*-
# @Time    : 2020/1/17  16:03
# @Author  : XiaTian
# @File    : 10_动态规划_斐波那契.py


# 子问题重复计算：递归思想
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)


# 动态规划思想（DP）:分解成子问题
def fibnacci_no_recurision(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


print(fibnacci(5))
print(fibnacci_no_recurision(5))