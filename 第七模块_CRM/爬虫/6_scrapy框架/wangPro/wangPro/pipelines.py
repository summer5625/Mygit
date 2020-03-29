# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WangproPipeline(object):

    # fp = None
    #
    # def open_spider(self, spider):
    #     self.fp = open('news.text', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        # self.fp.write(title + ':' + content + '\n')
        print(title, content, '\n')

        return item

    # def close_spider(self, spider):
    #
    #     self.fp.close()
