# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 19:20
# @Author  : XiaTian
# @File    : 服务端.py

'''
windows系统命令：
    1、dir 查看偶一个文件夹下的子文件夹和子文件
    2、ipconfig：查看本机网卡信息
    3、tasklist：查看运行的进程

Linux系统系的命令：
    1、ls
    2、ifconfig
    3、ps aux
'''
import socket
import subprocess
import struct
import json
import os

share_dir = r'D:\practice Python code\untitled\第三模块：面向对象&网络编程基础\网络编程\day4\服务端\share'

phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8081))
phone.listen(5)
print('start==>')
while True:
    conn,client_addr = phone.accept()
    print(client_addr)
    while True:  # 通信循环
        try:
            # 1、接收命令
            res = conn.recv(8096) # b'get a.txt'
            # 2、解析命令，提取相应的参数
            cmds = res.decode('utf-8').split() # ['get','a.txt']
            filename = cmds[1]
            # 3、以读的方式读取文件，读取文件内容发送给客户端

            # 1、制作固定长度报头
            header_dict = {
                            'filename':filename,
                            'md5':'xxxx',
                            'file_size':os.path.getsize(r'%s\%s'%(share_dir,filename))
                           }
            header_json = json.dumps(header_dict)
            header_bytes = header_json.encode('utf-8')

            # 2、发送报头长度
            conn.send(struct.pack('i',len(header_bytes)))

            # 3、发送报头
            conn.send(header_bytes)

            # 4、把真实数据发送给客户端
            with open(r'%s\%s'%(share_dir,filename), 'rb') as f:
                for line in f:
                    conn.send(line)

        except ConnectionResetError:
            break
    conn.close()
phone.close()

'''
    存在问题：
        1、服务端早制作报头时只讲要发送内容的长度发给客户端了，没有发送内容的其他描述信息
        2、如果服务端要发送的内容是个很大文件夹或者很大文件时，这是报头的容量就不够了
'''