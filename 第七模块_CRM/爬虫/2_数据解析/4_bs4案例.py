# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  16:06
# @Author  : XiaTian
# @File    : 4_bs4案例.py
from bs4 import BeautifulSoup
import requests


def soup(content):

    obj = BeautifulSoup(content, 'lxml')
    return obj


if __name__ == '__main__':

    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    # 获取标题
    pag_text = requests.get(url=url, headers=headers).text
    title_soup = soup(pag_text)
    a_list = title_soup.select('.book-mulu ul li a')
    fp = open('三国演义.text', 'w', encoding='utf-8')

    # 获取章节内容
    for a in a_list:

        title = a.string
        chapter_url = 'http://www.shicimingju.com' + a['href']
        chapter_text = requests.get(url=chapter_url, headers=headers).text
        chapter_soup = soup(chapter_text)
        chapter_content = chapter_soup.find('div', class_='chapter_content')
        content = chapter_content.text
        fp.write(title + content + '\n')
        print(title, '下载完成!')

