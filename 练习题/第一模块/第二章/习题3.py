#! -*- coding:utf-8 -*-
li=['alec','eric','rain']
#计算列表长度
print(len(li))
#列表添加seven
li.append('seven')
print(li)
#在第一个位置添加Tony
li.insert(0,"Tony")
print(li)
#修改第二个位置改为Kelly
li[1]='Kelly'
print(li)

#删除Eric
# b=li.pop(2)   # li.remove('eric')
# print(li)
# print(b)

#删除第二到第四的元素
# del li[1:3]
# print(li)
# #将列表反转
# li.reverse()
# print(li)

#输出列表的索引值for len  range
a=len(li)
b=range(0,a)
for i in b:
    print(i)
print(b)
for i,j in enumerate (li,100):
    print(i,j)