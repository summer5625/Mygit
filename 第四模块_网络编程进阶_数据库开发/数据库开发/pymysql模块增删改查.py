# # -*- coding: utf-8 -*-
# # @Time    : 2019/7/15  9:41
# # @Author  : XiaTian
# # @File    : pymysql模块增删改查.py
#
#
import pymysql
#
username = input('用户名:').strip()
# pwd = input('输入密码:').strip()
#
# # 建立连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='db1',
    charset='utf8')
#
# # 拿到游标,执行完毕返回的结果集默认以元组显示
cursor = conn.cursor()
#
# # 增
sql = 'insert into db1.userinfo(user,password) values(%s,%s)'
# rows = cursor.execute(sql,(username,pwd))  # 一次只能插一条
rows = cursor.executemany(sql,[('yuan1','123'),('wang2','123'),('zhan4','123')]) # 可以传多条数据
print(cursor.lastrowid)  # 查看插入前自增长的值到哪里了

#
# # 删
# sql = 'delete from db1.userinfo where id = %s'
# rows = cursor.execute(sql,(7))
# rows = cursor.executemany(sql,(4,5,6))
#
# # 改
#
# sql = 'update db1.userinfo set password = %s where id = %s'
# rows = cursor.execute(sql,('456',1))
# rows = cursor.executemany(sql,[('123',1),('456',2)])
#
# conn.commit()  # 插入完数据后，在关闭连接前必须执行这段数据才能插入进去
# #
# #
# cursor.close()
# conn.close()
#
#
# #  查询
#
# import pymysql
#
#
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='db1',
#     charset='utf8')
#
# cursor = conn.cursor()   # 查到结果以元组形式返回，不带字段名称
# cursor = conn.cursor(pymysql.cursors.DictCursor)  # 查询到结果单条以字典返回，多条以列表形式返回中带有字段名称
#
# rows = cursor.execute('select * from db1.userinfo;')
# print(cursor.fetchone())   # 获取一条记录
# print(cursor.fetchmany(2))   # 获取指定数量的多条记录
# print(cursor.fetchall())    # 获取所有记录
#
#
# # 光标绝对移动，移动时按照数据库数据的条数来算的
# cursor.scroll(2,mode='absolute')
# print(cursor.fetchone())
#
# # 光标的相对移动，相对有光标现在位置
# print(cursor.fetchone())
# cursor.scroll(-1,mode='relative')
# print(cursor.fetchone())
#
# cursor.close()
# conn.close()