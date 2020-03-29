# -*- coding: utf-8 -*-
# @Time    : 2019/12/3  17:05
# @Author  : XiaTian
# @File    : 6_国家药监总局.py
import requests
import json

if __name__ == '__main__':

    base_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    id_list = []
    all_data_list = []

    for pag in range(1,3):
        pag = str(pag)
        data = {
            'on': 'true',
            'page': pag,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }

        response = requests.post(url=base_url, data=data, headers=headers).json()
        for obj in response['list']:
            id_list.append(obj['ID'])

    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'

    for id in id_list:
        post_data = {
            "id": id
        }

        result = requests.post(url=post_url, data=post_data, headers=headers).json()
        all_data_list.append(result)

    fp = open('medicine.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)



















