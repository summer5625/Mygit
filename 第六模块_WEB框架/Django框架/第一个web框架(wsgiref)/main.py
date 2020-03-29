# -*- coding: utf-8 -*-
# @Time    : 2019/9/25  10:37
# @Author  : XiaTian
# @File    : main.py


from wsgiref.simple_server import make_server
from urls import url_patterns
from views import *


def application(environ,start_response):

    path = environ.get('PATH_INFO')
    start_response('200 OK', [])
    func = None
    print(path)
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break

    if func:
        return [func(environ)]
    else:
        return [b'404']


if __name__ == '__main__':
    http = make_server('127.0.0.1',8080,application)
    http.serve_forever()