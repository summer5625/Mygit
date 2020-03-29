# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  16:31
# @Author  : XiaTian
# @File    : 2_异步之线程池.py

import time
import requests
import re
from multiprocessing.dummy import Pool
from lxml import etree

# start_time = time.time()
#
#
# def get_page(str):
#
#     print('正在下载:', str)
#     time.sleep(2)
#     print('下载成功', str)
#
#
# name_list = ['summer', '芳华', '淑媛', '念念不忘']
#
# # 实例化线程池
# pool = Pool(4)
# pool.map(get_page, name_list)
#
# end_time = time.time()
#
# print(end_time - start_time)


# 爬取梨视频相关视频

url = 'https://www.pearvideo.com/category_5'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li/div/a')

urls = []

for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./@href')[0]
    video_title = li.xpath('./div[@class="vervideo-title"]/text()')[0] + '.mp4'

    # 获取试跑的播放地址
    video_text = requests.get(url=detail_url, headers=headers).text
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, video_text)[0]

    video_dict = {
        'title': video_title,
        'url': video_url
    }
    urls.append(video_dict)


def get_video(dic):

    print('正在下载:', dic['title'])
    video = requests.get(url=dic['url'], headers=headers).content

    with open(dic['title'], 'wb') as f:

        f.write(video)
    print('下载完成:', dic['title'])


pool = Pool(4)
pool.map(get_video, urls)
pool.close()
pool.join()
















