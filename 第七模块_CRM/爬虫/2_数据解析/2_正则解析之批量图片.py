# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  11:55
# @Author  : XiaTian
# @File    : 2_正则解析之批量图片.py
import requests
import re
import os

if __name__ == '__main__':

    if not os.path.exists('./funnyLibs'):
        os.mkdir('./funnyLibs')

    url = 'https://www.hahamx.cn/pic'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    pag_text = requests.get(url=url, headers=headers).text

    ex = '<div class="joke-main-content clearfix">.*?<img class="joke-main-img-suspend lazy" src="https://static.hahamx.cn/images/pic_none.png" data-original="(.*?)"/>.*?</div>'
    src_list = re.findall(ex, pag_text, re.S)

    for src in src_list:
        src = 'https:' + src
        img_data = requests.get(url=src, headers=headers).content

        img_path = './funnyLibs/' + src.split('/')[-1]

        with open(img_path,'wb') as f:
            f.write(img_data)
        print(src.split('/')[-1], ' 下载成功!')
