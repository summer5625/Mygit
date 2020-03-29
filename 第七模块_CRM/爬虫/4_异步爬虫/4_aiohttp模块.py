# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  22:35
# @Author  : XiaTian
# @File    : 4_aiohttp模块.py
import requests
import asyncio
import time

# aiohttp模块引出

# start = time.time()
# urls = [
#     'http://127.0.0.1:5000/summer',
#     'http://127.0.0.1:5000/jay',
#     'http://127.0.0.1:5000/tom'
# ]
#
#
# async def get_pag(url):
#
#     print('开始爬取:', url)
#
#     # requests.get()是基于同步进行页面爬取，必须使用异步网络请求进行异步爬取
#     response = requests.get(url=url)
#     print('爬取完成:', url)
#
# tasks = []
#
# for url in urls:
#
#     c = get_pag(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# print('总耗时:', time.time() - start)


# ###########使用aiohttp模块

import aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/summer',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]


async def get_pag(url):

    async with aiohttp.ClientSession() as session:

        # 此外还可以用post关键字发送post请求
        # 发送请求是所带的参数还和request模块中差不多：headers进行UA伪装
        # params/data分别对应get和post请求的参数
        # 使用代理时使用:  proxy='http://ip:端口'
        async with session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回json对象

            # 特别注意：在得到响应数据之前一定要用await进行手动挂起
            page_text = await response.text()
            print(page_text)


tasks = []

for url in urls:

    c = get_pag(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时:', time.time() - start)