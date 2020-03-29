# -*- coding: utf-8 -*-
# @Time    : 2019/5/24  23:05
# @Author  : XiaTian
# @File    : seven.py

import  socket
from multiprocessing import Process

def talk(conn):

    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionError:
            break
    conn.close()


def server(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    while True:
        conn,addr = server.accept()
        p = Process(target=talk, args=(conn,))
        p.start()


    server.close()

if __name__ == '__main__':

    server('127.0.0.1',8888)

