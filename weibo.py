# -*- coding: utf-8 -*-
# @Time    : 2020/1/18  19:18
# @Author  : XiaTian
# @File    : weibo.py
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import requests
import shutil
import time
from lxml import etree
import json
import asyncio
import aiohttp
import pymysql


'770页'
host = 'm.weibo.cn'
user_id = '5687069307'
base_url = 'https://%s/api/container/getIndex?' % host
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'


class MySQL:

    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '123456',
            database = 'weibo',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()

    def add(self, bids):
        # print(bids)
        sql = 'insert into weibo.articles(bid) values(%s)'
        self.cursor.executemany(sql, bids)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def get_single111(page):

    headers = {
        'Host': host,
        'Referer': 'https://m.weibo.cn/u/%s' % user_id,
        'User-Agent': user_agent
    }
    params = {
        'type': 'uid',
        'value': 7287854320,
        'containerid': int('107603' + user_id),  # containerid就是微博用户id前面加上107603
        'page': page
    }

    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)
# a = get_single111(47)
# print(a)

async def get_single(page):
    async with aiohttp.ClientSession() as session:
        headers = {
            'Host': host,
            'Referer': 'https://m.weibo.cn/u/%s' % user_id,
            'User-Agent': user_agent
        }
        params = {
            'type': 'uid',
            'value': 7287854320,
            'containerid': int('107603' + user_id),  # containerid就是微博用户id前面加上107603
            'page': page
        }

        url = base_url + urlencode(params)
        async with session.get(url, headers=headers) as response:
            # try:
            #     response = requests.get(url, headers=headers)
            #     if response.status_code == 200:
            #         data =  response.json()
            # except requests.ConnectionError as e:
            #     print('抓取错误', e.args)
            return await response.json()


def get_detail_id(data):
    # print(data)
    data = data.result()
    # print(data)
    if data:
        urls = data.get('data').get('cards')
        url_list = []
        id_list = []
        for url in urls:
            if str(url.get('card_type')) == '9':
                address = url.get('scheme')
                bid = url.get('mblog').get('bid')
                id_list.append(bid)
                url_list.append(address)
        # print(id_list)
        sql = MySQL()
        sql.add(id_list)
        # return url_list, id_list


def save_article_bid():
    # tasks = []
    loop = asyncio.get_event_loop()
    for i in range(200, 240):
        # t = get_single(i)
        task = asyncio.ensure_future(get_single(i))
        task.add_done_callback(get_detail_id)
        # tasks.append(task)
        loop.run_until_complete(task)

save_article_bid()

def get_detail(article_id):
    detail_url = 'https://m.weibo.cn/statuses/show?'
    header = {
        'Host': host,
        'User-Agent': user_agent,
    }
    params = {
        'id': article_id
    }
    url = detail_url + urlencode(params)
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)


# b = get_detail('Iq4GKBrVG')
# print(b.get('data').get('text'))
# print(b.get('data').get('created_at'))
def date_parser(date):
    date_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07',
                 'Aug': '08', 'Se': '09', 'Oct': '10', 'Nov': '11', 'Dec': 12}
    date_list = date.split(' ')
    time_temp = '%s-%s-%s'
    create_time = time_temp % (date_list[-1], date_dict[date_list[1]], date_list[2])
    return create_time


def detail_parser(data):

    article = {}

    pass


st = 'Sat Jan 18 18:04:24 +0800 2020'
# print(st.split(' '))





















