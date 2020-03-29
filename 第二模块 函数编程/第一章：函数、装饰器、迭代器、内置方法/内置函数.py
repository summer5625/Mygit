# 取列表中最大最小值
# a = [2, 5, 8, 3, 5, 6]
# min = min(a)
# max = max(a)
# print(min)
# print(max)
# a.sort()  # 正序排序
# print(a)

# sorted()自定义排序
# a = list(range(10))
# b = {}
# for i in a:
#     b[i] = i - 3
# b[5] = 20
# print(b)
# a = b.items()
# print(a)
#
# c = sorted(a, key=lambda x: x[1], reverse=True)
#
# print(c)

# eval()和exec()
# a = '1+2+3+4+5+6'
# f1 = eval(a)
# f2 = exec(a)
# print(f1,f2)

# ord和chr


# 求和sum
# a = [1,2,3,4,5,6]
# b=sum(a)
# print(b)
#


# bytearray用法
# s = 'aub大脸猫'
# s = s.encode('utf-8')
# s = bytearray(s)
# print(s)
# print(id(s))
# s[0] = 66
# s[4] = 163
# s = s.decode()
# print(s)
# print(id(s))


# map()和filter()

# 用map求取列表内，每个元素自乘
import functools

a = [1, 2, 3, 4, 5]
# map(lambda x: x*x,a)
# print(list(map(lambda x: x*x,a)))
#
# #用filter取出列表中符合筛选条件的值
# filter(lambda x: x>3, a)    #筛选出列表中中大于3的值
#
# print(list(filter(lambda x: x>3,a)))
#
# #reduce
#
b = functools.reduce(lambda x, y: x + y, a, 2)
print(b)
