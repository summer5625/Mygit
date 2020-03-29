# -*- coding: UTF-8 -*-
# @Time    : 2019/2/23 21:06
# @Author  : XiaTian
# @File    : prtice.txt.py
# @Software: PyCharm
# import os
# f = open(r'C:\Users\夏天\Desktop\02第二模块之三体语录','r+',encoding='utf-8')
# f2 = open(r'C:\Users\夏天\Desktop\02第二模块之三体语录.new','w',encoding='utf-8')
# a = f.readlines()
# del a[-1]
# for lin in a:
#     f2.write(lin)
# # for lin in f:
# #     if '25' in lin:
# #         lin = ''
# #     f2.write(lin)
# f.close()
# f2.close()
# os.remove(r'C:\Users\夏天\Desktop\02第二模块之三体语录')
# os.rename(r'C:\Users\夏天\Desktop\02第二模块之三体语录.new',r'C:\Users\夏天\Desktop\02第二模块之三体语录')

def prtice(func):
    ID = '000001'
    psw = 'abc123'
    def inner():
        id = input('id:').strip()
        password = input('password:').strip()
        if id == ID and password == psw:
            print('welcom')
            func()
    return inner

@prtice
def fun1():
    print('hello')

# fun1()




import time

a = time.time()
print(a)
b = a - a%86400-86400
c = a-a%86400-300
print(b)
lastday = time.gmtime(b)
neartoday = time.gmtime(c)
print(lastday)
print(neartoday)
b1 = round(b,7)
print(b1)