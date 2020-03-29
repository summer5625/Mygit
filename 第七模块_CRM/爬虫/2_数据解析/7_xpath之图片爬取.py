# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  18:26
# @Author  : XiaTian
# @File    : 7_xpath之图片爬取.py
import requests
import os
from lxml import etree


if __name__ == '__main__':
    if not os.path.exists('girls'):
        os.mkdir('girls')

    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    # 手动设定响应数据的编码格式
    # response.encoding = 'utf-8'
    pag_text = response.text

    tree = etree.HTML(pag_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    for li in li_list:
        title = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用处理中文乱码问题
        title = title.encode('iso-8859-1').decode('gbk')
        src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]

        img_content = requests.get(url=src, headers=headers).content
        img_path = './girls/' + title
        with open(img_path, 'wb') as f:
            f.write(img_content)
            print(title, '下载成功')
