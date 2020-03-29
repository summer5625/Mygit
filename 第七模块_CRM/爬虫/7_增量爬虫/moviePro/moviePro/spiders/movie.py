# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem


class MovieSpider(CrawlSpider):
    name = 'movie'

    start_urls = ['https://www.4567tv.tv/frim/index1.html']

    link = LinkExtractor(allow=r'frim/index1-\d+\.html')

    conn = Redis(host='127.0.0.1', port=6379)

    # detail_link = LinkExtractor(allow=r'Items/')
    rules = (
        Rule(link, callback='parse_item', follow=False),
        # Rule(detail_link, callback='parse_detail')
    )

    def parse_item(self, response):

        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')

        for li in li_list:

            detail_url = 'https://www.4567tv.tv/' + li.xpath('./div/a/@href').extract_first()

            # 将详情页面url存入redis的set中
            ex = self.conn.sadd('urls', detail_url)

            if ex == 1:

                print('该url没有被爬过')
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)

            else:

                print('该url被爬取过了')

    def parse_detail(self, response):

        title = response.xpaht('/html//div[1]/div/div/div/div[2]/h1/text()').extract_first()

        content = response.xpaht('/html//div[1]/div/div/div/div[2]/p[5]/span[2]//text()').extract()
        content = ''.join(content)

        item = MovieproItem()
        item['title'] = title
        item['content'] = content

        yield item
