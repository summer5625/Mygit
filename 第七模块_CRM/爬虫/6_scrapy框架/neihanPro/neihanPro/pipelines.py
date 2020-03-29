# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class NeihanproPipeline(object):

    fp = None

    # 再开始爬虫的时候只会被调用一次，用来打开要存储数据的文件
    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('neihan.text', 'w', encoding='utf-8')

    # 用来处理item类型的对象
    # 可以接收来自爬虫文件提交来的item对象
    # 该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":" + content + '\n')

        return item # 有返回值的话，就会将item传递给下一个即将被执行的管道类

    # 只在爬虫结束调用一次，用来关闭打开的文件
    def close_spider(self, spider):

        print('结束爬虫')
        self.fp.close()


# 管道文件中定义一个将数据存储到数据库的管道类
class MysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='spider', charset='utf8')

    def process_item(self, item, spider):

        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute("insert neihan(author, content) values('%s', '%s')" % (item['author'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):

        self.cursor.close()
        self.conn.close()