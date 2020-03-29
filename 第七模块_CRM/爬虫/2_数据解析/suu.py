# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  21:09
# @Author  : XiaTian
# @File    : suu.py
import requests
from lxml import etree

url = 'https://www.4568hh.com/vod/html9/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
pag_text = response.text

tree = etree.HTML(pag_text)

li_list = tree.xpath('//ul[@class="clearfix"]/li/a')
all_player = {}
for li in li_list:
    title = li.xpath('./@title')[0]
    hrf = 'https://www.4568hh.com' + li.xpath('./@href')[0]

    player_text = requests.get(url=hrf, headers=headers).text
    p_tree = etree.HTML(player_text)
    player_list = []
    player_url = p_tree.xpath('//ul[@class="playul"]/li/a/@href')

    all_path = []
    for url in player_url:
        url = "https://www.4568hh.com/" + url
        all_path.append(url)

    all_player[title] = all_path

# with open('老朱想要的.text', 'w', encoding='utf-8') as f:
#     f.write(str(all_player))
print(str(all_player))