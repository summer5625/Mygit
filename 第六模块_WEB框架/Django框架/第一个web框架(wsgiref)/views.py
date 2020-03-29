# -*- coding: utf-8 -*-
# @Time    : 2019/9/25  10:37
# @Author  : XiaTian
# @File    : views.py
from urllib.parse import parse_qs

from models import get_data


def index(environ):
    with open('./templates/1、vue起步.html','rb') as f:
        data = f.read()

    return data


def favicon(environ):
    with open('./templates/favicon.png','rb') as f:
        data = f.read()

    return data


def login(environ):
    with open('./templates/login.html','rb') as f:
        data = f.read()

    return data


def auth(environ):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH',0))
    except ValueError:
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    data = parse_qs(request_body)
    print(data)
    user = data.get(b"user")[0].decode("utf8")
    pwd = data.get(b"pwd")[0].decode("utf8")

    print(user,'----',pwd)
    cursor = get_data(user,pwd)
    print('数据库:', cursor)

    if cursor:

        return index(environ)
    else:
        return b'wrong username or password!'

#django-admin.exe