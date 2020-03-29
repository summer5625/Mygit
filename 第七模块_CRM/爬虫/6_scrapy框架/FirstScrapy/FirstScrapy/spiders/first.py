# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):

    # 爬虫文件名称：爬虫源文件的唯一标识
    name = 'first'

    # 允许的域名列表（一般注释掉）：用来限定start_urls列表中那些url可以进行请求发送
    # allowed_domains = ['www.baidu.com']

    # 起始的url列表：该列表存放的url会被scrapy自定进行请求的发送
    start_urls = ['http://www.baidu.com/']

    # 用作于数据解析：response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)
