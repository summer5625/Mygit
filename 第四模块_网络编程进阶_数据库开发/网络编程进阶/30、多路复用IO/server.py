# -*- coding: utf-8 -*-
# @Time    : 2019/6/4  23:27
# @Author  : XiaTian
# @File    : clients.py

from socket import *
import select
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(3)
server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8060))
server.listen(5)
server.setblocking(False)

rlist = [server,]  # 存建连接和收消息套接字
wlist = []  # 存发消息套接字
wdata = {}  # 存发送消息的内容
while True:

    '''
        参数依次为，收消息连接，发消息连接，异常连接，超时时间代表隔多长时间询问操作系统有无收到消息;
        返回收消息连接，发消息连接，出错连接
        
    '''
    rl,wl,xl = select.select(rlist,wlist,[],0.5)
    print('rl',rl)
    print('wl',wl)
    for sock in rl:
        if sock == server:
            conn,addr = sock.accept()
            rlist.append(conn)

        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in wl:
        data = wdata[sock]
        sock.send(data)
        wlist.remove(sock)
        wdata.pop(sock)

server.close()

