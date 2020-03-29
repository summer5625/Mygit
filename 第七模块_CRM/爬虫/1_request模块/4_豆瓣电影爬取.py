# -*- coding: utf-8 -*-
# @Time    : 2019/12/3  16:19
# @Author  : XiaTian
# @File    : 4_豆瓣电影爬取.py
import requests
import json


if __name__ == '__main__':

    url = 'https://movie.douban.com/j/chart/top_list'

    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': "",
        'start': 0,
        'limit': 20,
    }

    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/78.0.3904.108Safari/537.36"
    }

    response = requests.get(url=url, params=params, headers=headers)
    dic_obj = response.json()


    fp = open('douban.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)


