# -*- coding: utf-8 -*-
import scrapy
from imgPor.items import ImgporItem


class ImgesSpider(scrapy.Spider):
    name = 'imges'

    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):

        div_list = response.xpath('//div[@id="container"]/div')

        for div in div_list:

            # 使用伪属性，获取属性值
            src = div.xpath('./div/a/img/@src2').extract_first()
            item = ImgporItem()
            item['src'] = src

            yield item

