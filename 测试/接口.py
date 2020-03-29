# -*- coding: utf-8 -*-
# @Time    : 2020/1/3  18:47
# @Author  : XiaTian
# @File    : 接口.py
import requests
from lxml import etree
import urllib3


urllib3.disable_warnings()
s = requests.session()


def get_it_execution():
    result = {}

    login_url = 'https://account.chsi.com.cn/passport/login'

    h1 = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    s.headers.update(h1)
    r = s.get(login_url)
    dom = etree.HTML(r.content.decode('utf-8'))

    try:
        result['lt'] = dom.xpath('//input[@name="lt"]')[0].get('value')
        result['execution'] = dom.xpath('//input[@name="execution"]')[0].get('value')
        print(result)
    except:
        print('参数获取失败')

    return  result


def login(result, user='13812348888', pwd='123456'):
    login_url = 'https://account.chsi.com.cn/passport/login'

    h2 = {
        'Referer': login_url,
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Origin": '"https://account.chsi.com.cn"',
        # "Content-Length": 119,
        "Cache-Control": 'no-cache',
        "Upgrade-Insecure-Requests": '1',
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        'username': user,
        'password': pwd,
        'rememberMe': 'true',
        'lt': result['lt'],
        'execution': result['execution'],
        '_eventId': 'submit'
    }
    s.headers.update(h2)
    r4 = s.post(login_url, data=body)
    print(r4.text)


if __name__ == '__main__':
    result = get_it_execution()
    login(result, user='13812348888', pwd='123456')



















