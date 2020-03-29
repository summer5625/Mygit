# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  18:07
# @Author  : XiaTian
# @File    : 6_xpath之58二手房.py
import requests
from lxml import etree


if __name__ == '__main__':

    url = 'https://www.58.com/ershoufang/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    pag_text = requests.get(url=url, headers=headers).text

    # 数据解析
    tree = etree.HTML(pag_text)

    td_list = tree.xpath('//td[@class="t"]')

    # 持久化存储
    fp = open('58.text', 'w', encoding='utf-8')
    for td in td_list:

        # 局部解析
        title = td.xpath('./a/text()')[0]
        fp.write(title)