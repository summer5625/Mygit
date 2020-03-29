# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  16:23
# @Author  : XiaTian
# @File    : 1_同步爬虫.py

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

urls = [
    'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList',
    'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
    'https://image.hahamx.cn/2019/12/04/normal/2912165_dcd9713f02aefe46e30a8b5795fcfaff_1575389821.gif'
]


def get_content(url):
    print('正在爬取', url)
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:

        return response.content


def parse_content(content):

    print('响应长度为：', len(content))


for url in urls:

    content = get_content(url)
    parse_content(content)