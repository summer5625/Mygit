# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  16:39
# @Author  : XiaTian
# @File    : 1_request初识.py


import requests


# 爬取搜狗首页数据
if __name__ == '__main__':

    # 指定url
    url = 'https://www.sogou.com/'

    # 获取响应数据
    response = requests.get(url=url) # 发送get请求 requests.get(url, param, kwargs),三个参数
    a = requests.request()

    # 获取服务端相应数据
    page_text = response.text
    print(page_text)

    # 存储爬取页面数据
    with open('搜狗.html', 'w', encoding='utf-8') as fp:

        fp.write(page_text)

    print('爬取数据成功!!')

