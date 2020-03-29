#! -*- coding:utf-8 -*-
tu=('alex','eric','rain')
print(len(tu))
print(tu[1])
print(tu[0:2])
for i in tu:
    print(i)
a=len(tu)
b=range(0,a)
for i in b:
    print(i)
for i,j in enumerate (tu,10):
    print(i,j)