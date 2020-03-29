#print直接操作生成文件
# msg = '又回到最初的起点'
# f = open('print-file','w')
# print(msg,'开始重新打你的脸',sep='|',end='',file=f)

# #frozenset将集合变成不可变集合
# # # a = {1,2,3,4}
# # # a.discard(3)
# # # print(a)


#locals()打印函数中的局部变量
# age=25
# def f1():
#     age=18
#     print(age)
#     def f2():
#         age=26
#         print(age)
#     f2()
# print(locals())

#zip()将多个列表中的值一一对应成元组打印出来

# a = [1,2,3,4,5]
# b = ['a','b','c']
# d = [4,5,6]
#
# c=list(zip(a,b,d))
#
# print(c)

#round（）保留几位小数

a=1/3

print(round(a,3))