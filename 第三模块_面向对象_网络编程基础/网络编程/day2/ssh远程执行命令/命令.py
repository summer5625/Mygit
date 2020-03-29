# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:00
# @Author  : XiaTian
# @File    : 命令.py

# import os
import subprocess
# a = os.system('dir555')
# print(a)

obj = subprocess.Popen('dir1',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(obj)

b = obj.stdout.read().decode('GBK')
c = obj.stderr.read().decode('GBK')
print(b+c)