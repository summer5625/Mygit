# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlproPipeline(object):

    def process_item(self, item, spider):

        if item.__class__.__name__ == 'DetailItem':
            new_id = item['new_id']
            content = item['content']

        else:
            num = item['num']
            title = item['title']

        return item
