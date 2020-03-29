# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  19:08
# @Author  : XiaTian
# @File    : 8_xpath之城市名称爬取.py
import requests
from lxml import etree


if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    pag_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(pag_text)

    # hot_city = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
    # all_city = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')

    all_city_name = []

    # 可以两个过滤条件联合使用，相当于取两个结果的并集
    city_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for city in city_list:

        all_city_name.append(city.xpath('./text()')[0])

    print(all_city_name)