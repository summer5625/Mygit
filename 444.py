# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 23:56
# @Author  : XiaTian
# @File    : 444.py

'''QUEUE通信'''
# from multiprocessing import Queue, Process
# import time
#
# def task(name, q):
#
#     res = 'do {}'.format(name)
#     q.put(res)
#     time.sleep(1)
#
# def run(name, q):
#     while True:
#         data = q.get()
#         if data == None:break
#         print('{} {}'.format(name,data))
#         time.sleep(2)
#
# if __name__ == '__main__':
#     q = Queue()
#     t1 = Process(target=task, args=('t1', q))
#     t2 = Process(target=task, args=('t2', q))
#     r1 = Process(target=run, args=('r1', q))
#     r2 = Process(target=run, args=('r2', q))
#
#     t1.start()
#     t2.start()
#     r1.start()
#     r2.start()
#
#     t1.join()
#     t2.join()
#
#     q.put(None)
#     q.put(None)



'''写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间；'''

# from threading import Thread
# import time
#
#
# def task(name):
#     print('running {} time:{}'.format(name,time.time()))
#
#
# if __name__ == '__main__':
#     time.sleep(10)
#     for i in range(10):
#         t = Thread(target=task, args=('{}'.format(i),))


'''请使用pymsql模块连接你本地数据库，并向student表中插入一条数据'''

# import pymysql
#
# conn = pymysql.connect(
#         host = 'localhost',
#         port= 3306,
#         user = 'root',
#         password = '123456',
#         db ='db6',
#         charset = 'utf8'
# )
#
#
# cursor = conn.cursor()
#
# sql = 'INSERT student(sname,gender,credit) VALUES(%s,%s,%s)'
# cursor.execute(sql,('xia', '男', '123456'))
# conn.commit()
# cursor.close()
# conn.close()


# a = '123'
#
# print(a.isalpha()) # 字母
# print(a.isdigit()) # 数字


import sys

name = 'summer'

print(sys.getrefcount(name))

r_name = name

print(sys.getrefcount(name))

del r_name

print(sys.getrefcount(name))





















