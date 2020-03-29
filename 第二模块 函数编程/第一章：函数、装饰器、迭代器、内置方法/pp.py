def fib(max):
    a,b,n = 0,1,0
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return #


print(fib(5))
print(next(fib(5)))
print(next(fib(5)))
print(next(fib(5)))
print(next(fib(5)))