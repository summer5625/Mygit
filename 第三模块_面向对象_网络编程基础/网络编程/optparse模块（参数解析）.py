# -*- coding: utf-8 -*-
# @Time    : 2019/5/19  16:04
# @Author  : XiaTian
# @File    : optparse模块（参数解析）.py

import optparse

class  Ftp:

    def __init__(self):
        msg = ['1','2','-s','127.0.0.1','-P','3306','-u','xia','-p','123',]  # 必须为列表
        parse = optparse.OptionParser()
        parse.add_option('-s','--clients',dest='clients',help='ftp clients ip_addr')
        parse.add_option('-P','--port',type='int',dest='port',help='ftp clients port')
        parse.add_option('-u','--username',dest='username',help='username info')
        parse.add_option('-p','--password',dest='password',help='password info')
        self.options,self.args = parse.parse_args(msg)

        print(self.options)
        print(self.args)


if __name__ == '__main__':
    a = Ftp()

