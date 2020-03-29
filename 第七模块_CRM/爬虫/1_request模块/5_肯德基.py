# -*- coding: utf-8 -*-
# @Time    : 2019/12/3  16:54
# @Author  : XiaTian
# @File    : 5_肯德基.py
import requests
import json


if __name__ == '__main__':

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    data = {
        'cname': '',
        'pid': '',
        'keyword': '杭州',
        'pageIndex': '1',
        'pageSize': '10',
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    response = requests.post(url=url, data=data, headers=headers)
    dic_obj = response.json()

    fp = open('KFC.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)