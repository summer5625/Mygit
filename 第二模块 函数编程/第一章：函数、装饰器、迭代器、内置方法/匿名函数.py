from collections import Iterable
# def func(x,y):
#     if x<y:
#         return x*y
#     else:
#         return x/y
#
# f1=lambda x,y:x*y if x<y  else x/y #声明一个匿名函数,匿名函数只能用于简单逻辑运算和三元运算
#
# print(f1(56,6))

data = list (range(10))
# print(data)


# map用于普通函数
# def f2(x):
#     return x*x
# print(list(map(f2 ,data)))

# map与匿名函数联合使用
# print(list(map(lambda  x: x*x,data)))
#
# print(lambda b: b+2, data)

a = map(lambda  x: x*x,data)
# print(a)
# for i in a:
#     print(i)
print(isinstance(a, Iterable))


