# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  21:24
# @Author  : XiaTian
# @File    : 3_百度翻译.py

"""
破解百度翻译：
    -分析：
        --网页上砍，输入翻译字段后浏览器发送的是post请求
        --服务端响应的数据格式是个json格式

"""


import requests
import json


if __name__ == '__main__':

    # 得到url
    post_url = 'https://fanyi.baidu.com/sug'

    # UA伪装
    header = {
        "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/8.0.3904.108Safari/537.36"
    }

    # 获取url参数
    word = input("输入单词:")
    data = {
        "kw": word
    }

    # 发送请求
    response = requests.post(url=post_url, data=data, headers=header)

    # 获取响应数据
    dic_obj = response.json()

    print(dic_obj)

    # 持久化存储

    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

















