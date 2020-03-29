def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print('befor')
        yield b         #把函数的执行过程冻结在这一步，并且把b的值返回给外面的next
        a,b = b,a+b
        n = n+1
    return 'done'


f=fib(3)

print(next(f))
print(next(f))
print(next(f))