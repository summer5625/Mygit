# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlproItem(scrapy.Item):

    num = scrapy.Field()
    title = scrapy.Field()


class DetailItem(scrapy.Item):

    new_id = scrapy.Field()
    content = scrapy.Field()

