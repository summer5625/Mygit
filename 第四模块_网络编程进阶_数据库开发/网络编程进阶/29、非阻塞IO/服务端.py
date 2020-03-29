# -*- coding: utf-8 -*-
# @Time    : 2019/6/4  22:05
# @Author  : XiaTian
# @File    : 服务端.py

from socket import *
import select


server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8060))
server.listen(5)
server.setblocking(False)

rlist = []  # 每成功建立一个连接就存放到连接列表中
wlist = []  # 发消息连接列表
while True:

    try:
        conn,addr = server.accept()  # 在没有客户端启动情况下，服务端会阻塞住，直到有连接进来才会执行下一步
        print(addr)
        rlist.append(conn)  # 将建立成功的连接存放到连接列表中
        print(rlist)

    except BlockingIOError:

        # 收消息
        del_list = []  # 异常客户端连接列表
        for conn in rlist:
            try:             # 客户端在没有给服务端发消息时，服务端会在此处阻塞
                data = conn.recv(1024)
                if not data:
                    del_list.append(conn)  # 当接收到消息为空时，将客户端连接加入删除连接列表，然后继续循环下一个连接
                    continue
                # conn.send(data.upper())
                wlist.append((conn,data.upper())) # 将要发送给消息的客户端连接，和发送内容添加至发送消息列表
            except BlockingIOError:  # 客户端在没有给服务端发消息时,循环列表中的下一个连接
                continue

            except Exception:  # 当客户端断开后或者客户端异常，关闭连接，并将连接从rlist连接列表中移除
                conn.close()
                del_list.append(conn)  # 将断开客户端或者异常客户端连接加入要删除连接的列表
        # 发消息
        del_wlist = [] # 成功发送消息的客户端连接
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
                del_wlist.append(item)  # 消息发送成功后将，相应的客户端连接和消息放到要删除列表中
            except BlockingIOError:  # 由于系统内存有限，当要发送消息的连接太多，将系统内存占用完后，下面连接就无法正常发送消息给
                continue                  # 相应的客户端，则在下次循环时在将信息发送一遍

        for item in del_wlist:    # 删除成功发送消息的客户端连接
            wlist.remove(item)

        for conn in del_list:
            rlist.remove(conn)  # 删除无效连接


server.close()