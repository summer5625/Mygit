# -*- coding: utf-8 -*-
# @Time    : 2019/9/24  14:04
# @Author  : XiaTian
# @File    : 2、http请求协议.py

from socket import *

server = socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,addr = server.accept()
    data = conn.recv(1024)
    print(data)

    with open('login.html','rb') as f:
        sendd = f.read()

    conn.send(b'http/1.1 200 OK\r\n\r\n%s'%sendd)
    conn.close()













''''''
"""
一个请求组成：
请求首行
请求头  每个请求头之间用\r\n隔开
请求头
请求头
....
请求体数据 与请求头之间用\r\n\r\n隔开


get请求没有请求体
只有post请求才有请求体


b'GET / HTTP/1.1\r\n
Host: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n
Sec-Fetch-Site: none\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n'



b'GET /?name=summer&age=20 HTTP/1.1\r\n
Host: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n
Sec-Fetch-Site: none\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n



b'POST / HTTP/1.1\r\n
Host: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n
Content-Length: 20\r\n
Cache-Control: max-age=0\r\n
Origin: http://127.0.0.1:8080\r\n
Upgrade-Insecure-Requests: 1\r\n
Content-Type: application/x-www-form-urlencoded\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n
Sec-Fetch-Site: same-origin\r\n
Referer: http://127.0.0.1:8080/\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n
user=summer&pwd=5689'

"""