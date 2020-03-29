# -*- coding: utf-8 -*-
# @Time    : 2019/7/20  13:54
# @Author  : XiaTian
# @File    : server.py


from socket import *
import select

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8070))
server.listen(5)
server.setblocking(False) # 设置是否阻塞，False代表不阻塞

c_list = [server,]
w_list = []
w_data = {}
while True:
    cl, wl, xl = select.select(c_list, w_list, [], 0.5)
    for conn in cl:
        if conn == server:
            conn, addr = conn.accept()
            c_list.append(conn)
        else:
            try:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    c_list.remove(conn)
                    continue
                w_list.append(conn)
                w_data[conn] = data.upper()

            except ConnectionError:
                conn.close()
                c_list.remove(conn)

    for conn in wl:
        data = w_data[conn]
        conn.send(data)
        w_list.remove(conn)
        w_data.pop(conn)

server.close()















