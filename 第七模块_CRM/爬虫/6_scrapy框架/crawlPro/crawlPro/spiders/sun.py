# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlPro.items import CrawlproItem, DetailItem


class SunSpider(CrawlSpider):
    name = 'sun'

    start_urls = ['http://wz.sun0769.com/html/top/report.shtml'] # http://wz.sun0769.com/index.php/question/report?page=

    # 连接提取器：根据指定的规则（正则表达式）进行指定的连接提取
    # allow=‘正则表达式’，即指定的匹配链接的规则
    link = LinkExtractor(allow=r'page=\d+')
    link_detail = LinkExtractor(allow=r'html/question/\d+/\d+\.shtml')
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则的解析操作
        # callback是指定的解析器
        Rule(link, callback='parse_item', follow=False),
        Rule(link_detail, callback='parse_detail')
    )

    def parse_item(self, response):

        # xpath里面不能有tbody，否则匹配不上
        # tr_list = response.xpath('/html/body/div[8]/table[2]/tbody/tr')
        tr_list = response.xpath('/html/body/div[8]/table[2]//tr')

        for tr in tr_list:
            item = CrawlproItem()
            num = tr.xpath('./td[1]/text()').extract_first()
            title = tr.xpath('./td[3]/a/@title').extract_first()
            item['num'] = num
            item['title'] = title

            yield item

    def parse_detail(self, response):

        new_id = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        new_id = new_id.split(':')[-1]
        content = response.xpath('/html/body/div[9]/table[2]//tr[1]/td//text()').extract()
        content = ''.join(content)
        item = DetailItem()
        item['new_id'] = new_id
        item['content'] = content

        yield item

