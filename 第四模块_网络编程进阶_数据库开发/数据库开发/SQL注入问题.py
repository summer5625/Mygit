# -*- coding: utf-8 -*-
# @Time    : 2019/7/15  9:34
# @Author  : XiaTian
# @File    : SQL注入问题.py

import pymysql

username = input('用户名:').strip()
password = input('输入密码:').strip()

# 建立连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='db1',
    charset='utf8')

# 拿到游标,执行完毕返回的结果集默认以元组显示
cursor = conn.cursor()

# 执行sql语句
sql = "select * from db1.userinfo where user = %s and password = %s"

rows = cursor.execute(sql, (username, password))  # 以元组形式传参

# 关闭连接
cursor.close()
conn.close()

if rows:
    print('登录成功!')
else:
    print('登录失败!')
