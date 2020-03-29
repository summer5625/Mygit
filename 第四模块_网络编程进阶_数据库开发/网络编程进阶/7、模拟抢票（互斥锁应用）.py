# -*- coding: utf-8 -*-
# @Time    : 2019/5/25  0:34
# @Author  : XiaTian
# @File    : 7、模拟抢票（互斥锁应用）.py

import time
import json
from multiprocessing import Process,Lock

def search(name):
    time.sleep(1)
    dic = json.load(open('db.txt','r',encoding='utf-8'))
    print('<%s> 查看到剩余票数 【%s】'%(name,dic['count']))

def get(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    if int(dic['count']) > 0:
        dic['count'] = int(dic['count']) - 1
        time.sleep(3)
        json.dump(dic,open('db.txt','w',encoding='utf-8'))
        print('<%s>抢票成功'%name)
    else:
        print('余票不足!')

def run(name,lock):
    search(name)
    lock.acquire()
    get(name)
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):

        p = Process(target=run,args=('路人%s'%i,lock))
        p.start()

# a = {'count':1}
# json.dump(a,open('db.txt','w',encoding='utf-8'))

'''
join是将代码整体编程串行，而互斥锁时将代码的部分内容编程串行
'''