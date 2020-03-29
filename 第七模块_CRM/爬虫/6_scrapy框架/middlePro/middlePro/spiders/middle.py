# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'

    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):

        content = response.text

        with open('fp.html', 'w', encoding='utf-8') as f:
            f.write(content)
