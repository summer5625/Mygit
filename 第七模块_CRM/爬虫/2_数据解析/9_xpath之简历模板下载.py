# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  19:50
# @Author  : XiaTian
# @File    : 9_xpath之简历模板下载.py
import requests
from lxml import etree


if __name__ == '__main__':

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    for i in range(0,3):

        if i == 0:
            url = 'http://sc.chinaz.com/jianli/free.html'
        else:
            url = 'http://sc.chinaz.com/jianli/free_%s.html' % i

        pag_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(pag_text)
        pag_list = tree.xpath('//div[@id="container"]/div/a/@href')

        for resume in pag_list:
            content_text = requests.get(url=resume, headers=headers).text
            resume_tree = etree.HTML(content_text)
            download_url = resume_tree.xpath('//ul[@class="clearfix"]/li/a/@href')[0]
            file_name = download_url.split("/")[-1]
            file_path = './jianli/' + file_name
            file = requests.get(url=download_url, headers=headers).content

            with open(file_path, 'wb') as f:
                f.write(file)
