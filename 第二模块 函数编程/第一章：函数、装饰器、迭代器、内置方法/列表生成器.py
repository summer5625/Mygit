
# a=map(lambda x:x+1,a)
# for i in a:
#     print(i)
# a=range(10)
# a = [i+1 for i in a]
# print(a)

#
# a = (i for i in range(10))
# next(a)    #一个个调用


#调用方

# while True:
#     print(next(a))

#while循环调用程序会报错
#for循环调用则不会出错

# for i in a:
#     print(i)
#
#
# b = range(10)
# print(b)

def range(n):
     count = 0
     while count < n:
         print('count',count)
         count+=1
         singel = yield count
         if singel == 'stop':
             break
     return 555

new_range = range(10)

next(new_range)
next(new_range)
next(new_range)

# new_range.send('stop')
# print(next(new_range))
