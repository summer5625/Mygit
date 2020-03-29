
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26  22:20
# @Author  : XiaTian
# @File    : 8、队列.py

from multiprocessing import Queue

q = Queue(3)  # 规定队列的容量，队列中适合放较小的数据，当里面不填时代表队列可以无穷存放数据

q.put('hahah') # 向队列中存放数据，存放数据数量不能超过队列的容量,队列满后再向里面存放数据程序会卡住，直到数据被取走
q.put([1,2,3])
q.put({'a':123})

print(q.full())  # 判断队列是否满了

print(q.get())  # 从队列中取数据，队列取数据遵循先进先出原则。当取得数据量超过队列容量时程序会卡住，直到在次存放数据
print(q.get())
print(q.get())
print(q.empty())  # 判断队列是否空了