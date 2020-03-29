# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  21:50
# @Author  : XiaTian
# @File    : 3_协程基础.py
# import asyncio
#
#
# async def request(url):
#
#     print('正在请求：', url)
#
#     print('请求成功', url)
#
#     return url
#
# f = request('www.baidu.com')

# 事件循环event_loop
# loop = asyncio.get_event_loop()

# 将协程对象注册到事件循环中
# loop.run_until_complete(f)

# # 使用task
# loop = asyncio.get_event_loop()
# # 创建task对象
# task = loop.create_task(f)
# print(task)
#
# # 执行task
# loop.run_until_complete(task)
# print(task)

# future使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(f)
#
# print(task)
# loop.run_until_complete(task)
# print(task)


# 回调机制
# def callback_func(task):
#
#     # result()返回的是任务对象中封装的协程对象对应的函数的返回值
#     print(task.result())

# 绑定回调

# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(f)
#
# # 将回调函数绑定到任务对象中
# task.add_done_callback(callback_func)
# loop.run_until_complete(task)


# 多任务异步协程

import asyncio
import time


async def request(url):
    print('正在请求：', url)

    # 同步操作，在异步协程中如果出现同步模块代码，那么则无法实现异步
    # time.sleep(2)

    # 当在asyncio中遇到阻塞操作必须手动进行挂起
    await asyncio.sleep(2)

    print('请求成功', url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.luffycity.com',
    'www.pearvideo.com'
]

# 构建任务列表，存放多个任务
tasks = []
for url in urls:

    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start)


















