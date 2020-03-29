# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  17:04
# @Author  : XiaTian
# @File    : 2_网页采集器.py

import requests

if __name__ == '__main__':
    # 指定url
    url = 'https://www.sogou.com/web'

    kw = input('enter a word:')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }

    # 获取输入的url参数
    param = {
        'query': kw
    }

    # 获取响应数据 param:url的参数   headers：UA伪装请求头
    response = requests.get(url=url, params=param, headers=headers)

    # 获取响应数据
    page_text = response.text

    # 存储数据
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName, '爬取成功!')

"""
UA伪装：

    UA：http协议中的User-Agent请求头，是请求载体的身份标识
    UA检测：是门户网站的服务器会检测对应的请求载体的身份标识，如果检测到请求载体的身份标识为某一款浏览器，则说明该请求是一个正常请求。
    但是，如果检测到请求载体不是某一款浏览器，则表示该请求不一个正常的请求，则服务端就很可能拒绝该次请求
    
    UA伪装：

"""
