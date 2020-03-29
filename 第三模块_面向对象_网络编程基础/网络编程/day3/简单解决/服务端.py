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

phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8081))
phone.listen(5)
print('start==>')
while True:
    conn,client_addr = phone.accept()
    print(client_addr)
    while True:  # 通信循环
        try:

            cmd = conn.recv(1024)
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 1、制作固定长度报头
            total_size = len(stderr) + len(stdout)
            header_dict = {'filename':'a.txt','md5':'xxxx','total_size':total_size}
            header_json = json.dumps(header_dict)
            header_bytes = header_json.encode('utf-8')

            # 2、发送报头长度
            conn.send(struct.pack('i',len(header_bytes)))

            # 3、发送报头
            conn.send(header_bytes)

            # 4、把真实数据发送给客户端
            conn.send(stdout + stderr)

        except ConnectionResetError:
            break
    conn.close()
phone.close()

'''
    存在问题：
        1、服务端早制作报头时只讲要发送内容的长度发给客户端了，没有发送内容的其他描述信息
        2、如果服务端要发送的内容是个很大文件夹或者很大文件时，这是报头的容量就不够了
'''