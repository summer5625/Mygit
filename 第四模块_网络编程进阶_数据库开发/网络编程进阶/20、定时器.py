# -*- coding: utf-8 -*-
# @Time    : 2019/5/30  0:20
# @Author  : XiaTian
# @File    : 20、定时器.py

import random
from threading import Timer

# def task(name):
#     print('hello %s'%name)
#
# if __name__ == '__main__':
#     t = Timer(5,task,args=('liu',))
#     t.start()

class Code:

    def __init__(self):
         self.make_cache()

    def make_cache(self,interval=5):
        self.cache = self.make_code()
        print(self.cache)
        self.t = Timer(interval,self.make_cache)
        self.t.start()

    def make_code(self,n=5):
        res = ''
        for i in range(n):
            s1 = str(random.randint(0,9))
            s2 = chr(random.randint(65,90))
            res += random.choice([s1,s2])

        return res

    def check(self):
        while True:
            code = input('请输入验证码>>:').strip()
            if code.upper() == self.cache:
                print('验证码输入正确!')
                self.t.cancel()
                break

obj = Code()
obj.check()


