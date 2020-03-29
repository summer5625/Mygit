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
            header = struct.pack('i',total_size)
            # 2、把报头（固定长度）发送给客户端
            conn.send(header)
            conn.send(stdout + stderr)
        except ConnectionResetError:
            break
    conn.close()
phone.close()
