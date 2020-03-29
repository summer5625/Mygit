#函数作为参数
def func(x,y):
    return x**y
def func2(a,b):
    return a+b

f = func2(func)   #高阶函数，貌似func2中只能有一个变量，两个变量时会报错

print(f(2,3))

#函数作为返回值
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax = ax + n
        return ax
    return sum

a=lazy_sum(1,2,3)
print(a())