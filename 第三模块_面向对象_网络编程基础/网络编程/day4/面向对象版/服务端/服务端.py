# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 10:15
# @Author  : XiaTian
# @File    : 服务端.py


import socket
import struct
import json
import os

class MYTCPServer:
    address_family = socket.AF_INET     # 套接字家族

    socket_type = socket.SOCK_STREAM    # 套接字传输协议

    allow_reuse_address = False         # 是否重用端口

    max_packet_size = 8192              # 一次最多传输多少

    coding='utf-8'                      # 编码格式

    request_queue_size = 5              # 报头长度

    server_dir='file_upload'            # 服务端共享文件地址

    def __init__(self, server_address, bind_and_activate=True):
        """得到套接字对象"""
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate: # 判断对象是否绑定被激活
            try:
                self.server_bind()         # 绑定IP和端口
                self.server_activate()     #
            except:
                self.server_close()        # 没被激活，则关闭
                raise

    def server_bind(self):
        """Called by constructor to bind the socket.
        """
        if self.allow_reuse_address:  # 判断ip和端口是否能被重用
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)  # 绑定IP和端口
        self.server_address = self.socket.getsockname()  # 获取当前的地址
        print(self.server_address)

    def server_activate(self):
        """Called by constructor to activate the clients.
        """
        self.socket.listen(self.request_queue_size)  # 监听

    def server_close(self):
        """Called to clean-up the clients.
        """
        self.socket.close()  # 关闭套接字

    def get_request(self):
        """Get the request and servers address from the socket.
        """
        return self.socket.accept()   # 与客户端握手建立连接

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()

    def run(self):
        while True:
            self.conn,self.client_addr=self.get_request()
            print('from servers ',self.client_addr)
            while True:
                try:
                    head_struct = self.conn.recv(4)  # 接收报头
                    if not head_struct:break

                    head_len = struct.unpack('i', head_struct)[0]
                    head_json = self.conn.recv(head_len).decode(self.coding)
                    head_dic = json.loads(head_json)

                    print(head_dic)
                    #head_dic={'cmd':'put','filename':'a.txt','filesize':123123}
                    cmd=head_dic['cmd']
                    if hasattr(self,cmd):
                        func=getattr(self,cmd)
                        func(head_dic)
                except Exception:
                    break

    def put(self,args):
        file_path=os.path.normpath(os.path.join(
            self.server_dir,
            args['filename']
        ))

        filesize=args['filesize']
        recv_size=0
        print('----->',file_path)
        with open(file_path,'wb') as f:
            while recv_size < filesize:
                recv_data=self.conn.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size+=len(recv_data)
                print('recvsize:%s filesize:%s' %(recv_size,filesize))


tcpserver1=MYTCPServer(('127.0.0.1',8080))

tcpserver1.run()