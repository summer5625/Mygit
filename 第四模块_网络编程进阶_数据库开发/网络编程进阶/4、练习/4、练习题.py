# -*- coding: utf-8 -*-
# @Time    : 2019/5/23  0:26
# @Author  : XiaTian
# @File    : 4、练习题.py

# from multiprocessing import Process
# import time
# import random
#
# def task(name):
#     print('%s is piaoing' %name)
#     time.sleep(random.randrange(1,5))
#     print('%s is piao end' %name)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=('egon',))
#     p1.start()
#
#     p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
#     print(p1.is_alive()) #结果为True
#
#     print('主')
#     print(p1.is_alive()) #结果为False


from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    p3.start()
    p3.join()

    print('-------->4')



    '''
       -------->4
       -------->1
       -------->3
       -------->2
    '''