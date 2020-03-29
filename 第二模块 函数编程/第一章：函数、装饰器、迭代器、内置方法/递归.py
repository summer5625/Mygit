#递归函数名称recursion
# import sys
#
# print(sys.getrecursionlimit())  #查看python中默认的递归次数，一般是1000次
# sys.setrecursionlimit(1500)     #修改递归次数
# def recursion(n):    #python中限制了递归的次数，也可以修改递归的次数
#     print(n)
#     recursion(n+1)
# recursion(1)










#实现一个数除以另外一个数，直到结果为0

# def cala(n):
#      a = int(n/2)
#      print(a)
#      if a == 0:
#          returna
#      cala(a)
#      print(a)
# cala(10)



#计算阶乘

def cla(n):

    if n==1:
        return 1

    return n*cla(n-1)

print(cla(5))

#尾递归优化
def cla(n):
    print(n)

    return cla(n+1)

cla(1)