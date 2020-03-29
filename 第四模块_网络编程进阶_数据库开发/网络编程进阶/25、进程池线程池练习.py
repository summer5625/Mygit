# -*- coding: utf-8 -*-
# @Time    : 2019/6/1  22:45
# @Author  : XiaTian
# @File    : 25、进程池线程池练习.py

import requests
from concurrent.futures import ProcessPoolExecutor

response = requests.get('https://www.cnblogs.com/linhaifeng/')  # 去目标站点下载文件


def get(url):
    print('get %s'%url)
    response = requests.get(url)

    return {'url':url,'content':response.text}


def parse(res):
    res = res.result()
    print('%s parse res is %s'%(res['url'],len(res['content'])))


if __name__ == '__main__':
    urls = [
            'https://www.cnblogs.com/linhaifeng/articles/6817679.html',
            'https://www.baidu.com/',
            'http://mail.hichina.com/alimail/auth/login?reurl=%2Falimail%2F'
    ]

    pool = ProcessPoolExecutor(2)
    for url in urls:
        pool.submit(get,url).add_done_callback(parse)