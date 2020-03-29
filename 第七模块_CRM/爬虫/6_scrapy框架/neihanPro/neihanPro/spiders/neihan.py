# -*- coding: utf-8 -*-
import scrapy
from neihanPro.items import NeihanproItem


class NeihanSpider(scrapy.Spider):
    name = 'neihan'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.budejie.com/']

    # ########################基于终端指令进行持久化存储########################
    # def parse(self, response):
    #
    #     # 解析作者名和段子内容
    #     li_list = response.xpath('//div[@class="j-r-list"]/ul/li')
    #     all_data = []
    #
    #     for li in li_list:
    #
    #         # xpaht返回的是一个列表，但列表元素是selector对象
    #         # extract()可以将selector对象中的data参数存储的字符串提取出来
    #         # author = li.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/a/text()')[0].extract()
    #
    #         # extract_first()只有在确定列表中只有一个元素时才使用
    #         author = li.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/a/text()').extract_first()
    #         # 列表调用了extract()之后，则表示将列表中的每一个selector对象中的data对应的字符串提取出来
    #         content = li.xpath('./div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()').extract()
    #         content = ''.join(content)
    #
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #
    #         all_data.append(dic)
    #
    #     return all_data

    # ########################基于管道进行持久化存储########################

    def parse(self, response):

        # 解析作者名和段子内容
        li_list = response.xpath('//div[@class="j-r-list"]/ul/li')
        all_data = []

        for li in li_list:

            # xpaht返回的是一个列表，但列表元素是selector对象
            # extract()可以将selector对象中的data参数存储的字符串提取出来
            # author = li.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/a/text()')[0].extract()

            # extract_first()只有在确定列表中只有一个元素时才使用
            author = li.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/a/text()').extract_first()
            # 列表调用了extract()之后，则表示将列表中的每一个selector对象中的data对应的字符串提取出来
            content = li.xpath('./div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()').extract()
            content = ''.join(content)

            item = NeihanproItem()
            item['author'] = author
            item['content'] = content

            # 将item提交给管道
            yield item
