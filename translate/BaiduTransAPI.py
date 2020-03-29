# -*- coding: utf-8 -*-
# @Time    : 2020/3/9  17:22
# @Author  : XiaTian
# @File    : BaiduTransAPI.py
import http.client
import hashlib
import urllib
import random
import json

def translate(fromLang, toLang, content):
    appid = '20200309000395319'  # 填写你的appid   20200309000395319
    secretKey = 'Joa597fHXjWzqmI0eXMC'  # 填写你的密钥
    result = None

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = fromLang   #原文语种
    toLang = toLang   #译文语种
    salt = random.randint(32768, 65536)
    q= content
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

    except Exception as e:
        result = e
    finally:
        if httpClient:
            httpClient.close()

    return result


