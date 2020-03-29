# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 20:46
# @Author  : XiaTian
# @File    : my_moudle.py
# @Software: PyCharm



# # eval()
# s = '1+2+3+4'
# a = eval(s)
# print(a)
#
# # exec()
# b = exec(s)
# print(b)
#
#
# ss = '1+2+3+4+5' \
#      '4+5+6+7'
#
# exec(ss)
# print(eval(ss))
#
# c = 1/3
# print(round(c,6))    # 6表示要保留6小位数
#
# a = 6
# b = 4
# print(divmod(a,b))  # 结果为（1,2）其中1代表商，2代表余数
#
# d = 5
# print(pow(d,3))     # 其中3代表求取5的3次幂
#
# f = [2,2,3,4]
# print(sum(f))       # sum()函数括号里面的必须为可迭代对象
#
# l = [3,1,2,2]
# h = min(f,l)       # 如果是两个列表，只比较列表第一个元素大小
# print(h)


# a = range(0,9)
# b = map(lambda x:x*x,a)
# print(next(b))
#
# # 这段代码
# def calc(n):
#     return n ** n
#
#
# print(calc(10))
#
# # 换成匿名函数
# calc = lambda n: n ** n
# print(calc(10))

import time

a = time.gmtime()
print(a)

b = time.time()
print(b)

c = time.localtime()
print(c)