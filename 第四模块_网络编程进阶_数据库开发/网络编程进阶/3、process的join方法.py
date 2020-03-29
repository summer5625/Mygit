# -*- coding: utf-8 -*-
# @Time    : 2019/5/21  0:26
# @Author  : XiaTian
# @File    : 3、process的join方法.py

'''join方法是在一个进程结束后下一个进程才会执行'''

from multiprocessing import Process
import time,os

# os.getpid()查看子进程id,os.getppid()查看父进程id
class MyProcess(Process):
    '''创建一个类来继承Process类'''

    def __init__(self,name,n):

        super().__init__()  # 重用继承父类的方法
        self.name = name
        self.n = n

    def run(self):
        '''创建的方法名称必须叫run()'''
        print('%s is running ；process id is %s ；parent id is %s' % (self.name,os.getpid(),os.getppid()))
        time.sleep(self.n)
        # print('%s is end,end id is %s' % (self.name,os.getpid()))

# 多进程并发
# if __name__ == '__main__':
#     start = time.time()
#     p1 = MyProcess('子进程1',5)
#     p2 = MyProcess('子进程2',4)
#     p3 = MyProcess('子进程3',3)
#     p4 = MyProcess('子进程4',2)
#     p5 = MyProcess('子进程5',1)
#
#     p1.start()  # 调用的是自定义类中的run方法
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#
#     p.join()
#     print('process id is %s ; father id is %s'%(os.getpid(),os.getppid()))
#     print('主',time.time()-start)
#     print(p.is_alive())  # 查看进程是否在执行
#     print(p.pid)  # 查看结束掉后的僵尸进程p的pid

# 多进程串行
# if __name__ == '__main__':
#     start = time.time()
#     p1 = MyProcess('子进程1',5)
#     p2 = MyProcess('子进程2',4)
#     p3 = MyProcess('子进程3',3)
#     p4 = MyProcess('子进程4',2)
#     p5 = MyProcess('子进程5',1)
#
#     p1.start()  # 调用的是自定义类中的run方法
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     p4.start()
#     p4.join()
#     p5.start()
#     p5.join()
#
#
#     # p.join()
#     print('process id is %s ; father id is %s'%(os.getpid(),os.getppid()))
#     print('主',time.time()-start)
#



n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了

def work():
    global n
    n=0
    print('子进程内: ',n)


if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    print('主进程内: ',n)