# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider # 导入scrapy_redis
from fbsPro.items import FbsproItem


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'fbs'
    link = LinkExtractor(allow=r'page=\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('/html/body/div[8]/table[2]//tr')

        for tr in tr_list:
            item = FbsproItem()
            num = tr.xpath('./td[1]/text()').extract_first()
            title = tr.xpath('./td[3]/a/@title').extract_first()
            item['num'] = num
            item['title'] = title

            yield item
