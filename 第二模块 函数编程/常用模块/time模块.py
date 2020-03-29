import time
x=time.time()   #打印当前时间
print(x)

y=time.localtime()   #打印当地时间
print(y)
#
# print('%s-%s-%s'%(y.tm_year ,y.tm_mon ,y.tm_wday))
#
# # c= time.gmtime()
# # print(c)
#
a = time.localtime(14589657000)   #将时间对象转换成时间戳（既年月日结构）
#
# print(a)
#
# b = time.mktime(y)    #将时间戳转换成时间对象
# print(b)
#
# d = time.strftime('%Y-%m-%d',a)
# print(d)

# import  datetime
# x=datetime.datetime.now()
# print(x)
# y=datetime.timedelta(minutes=20)  #时间运算
# t=x+y
# print(t)
#
# r = x.replace(2016,month=2)
# print(r)

# x = time.time()
# g = time.localtime(x)
# k = time.strftime('%Y-%m-%d',g)
# print(k)