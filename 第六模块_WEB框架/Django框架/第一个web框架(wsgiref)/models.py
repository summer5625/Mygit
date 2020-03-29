# -*- coding: utf-8 -*-
# @Time    : 2019/9/25  10:37
# @Author  : XiaTian
# @File    : models.py

import pymysql


def get_data(user,password):

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='frist_web',
        charset='utf8'
    )

    cursor=conn.cursor()
    sql = 'select * from userinfo where username="%s" and password="%s"' % (user,password)
    cursor.execute(sql)
    a = cursor.fetchall()
    return a



