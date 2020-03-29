# -*- coding: utf-8 -*-
# @Time    : 2019/5/30  22:24
# @Author  : XiaTian
# @File    : 21、进程Queue.py

import queue

# q = queue.Queue(3)
# q.put('one')
# q.put('two')
# q.put('three')
# q.put(4,block=False)  # 设置队列然后再放值进去队列是否阻塞；Ture为阻塞，False为不阻塞，当超过队列容量就会报错
# q.put(4,block=True,timeout=3) # 设置阻塞的超时时间，超多多少时间就报错

# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False))  # 设置取队列值是否阻塞
# print(q.get_nowait())  # 等同于q.get(block=False)
# print(q.get(block=True,timeout=3))


# d = queue.LifoQueue(3) # 后进先出，堆栈
# d.put('one')
# d.put('two')
# d.put('three')
# d.put(4,block=True,timeout=3)

# print(d.get())
# print(d.get())
# print(d.get())
# print(d.get(block=True,timeout=3))

q = queue.PriorityQueue()  # 优先级队列，可以设置队列优先级，优先级高的先出来

q.put((10,'one'))   # 数字越小优先级越高
q.put((30,'two'))
q.put((20,'three'))

# q.put([10,'1'])
# q.put([30,'2'])
# q.put([20,'3'])



print(q.get())
print(q.get())
print(q.get())


