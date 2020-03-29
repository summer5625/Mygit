# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  15:31
# @Author  : XiaTian
# @File    : 9_代理IP爬取.py
import requests


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    # 使用代理ip爬取
    response = requests.get(url=url, headers=headers, proxies={'https':'110.243.24.248:9999'})  # proxies={'https':'110.243.24.248:9999'}
    response.encoding = 'utf-8'
    pag = response.text

    with open('ip.html', 'w', encoding='utf-8') as f:
        f.write(pag)