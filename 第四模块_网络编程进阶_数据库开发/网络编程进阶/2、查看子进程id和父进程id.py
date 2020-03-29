# -*- coding: utf-8 -*-
# @Time    : 2019/5/21  0:10
# @Author  : XiaTian
# @File    : 2、查看子进程id和父进程id.py


from multiprocessing import Process
import time,os

# os.getpid()查看子进程id,os.getppid()查看父进程id
class MyProcess(Process):
    '''创建一个类来继承Process类'''

    def __init__(self,name):

        super().__init__()  # 重用继承父类的方法
        self.name = name

    def run(self):
        '''创建的方法名称必须叫run()'''
        print('%s is running ；process id is %s ；parent id is %s' % (self.name,os.getpid(),os.getppid()))
        time.sleep(3)
        print('%s is end,end id is %s' % (self.name,os.getpid()))


if __name__ == '__main__':
    p = MyProcess('子进程1')
    p.start()  # 调用的是自定义类中的run方法

    print('process id is %s ; father id is %s'%(os.getpid(),os.getppid()))