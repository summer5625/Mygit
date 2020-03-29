# -*- coding: utf-8 -*-
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']
    url = 'http://www.521609.com/daxuexiaohua/list3%s.html'
    page_num = 2

    def parse(self, response):

        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')

        for li in li_list:

            title = li.xpath('./a[2]/b/text() | ./a[2]/text()').extract_first()
            print(title)

        # 手动发送请求
        if self.page_num <= 11:
            new_url = self.url % self.page_num
            self.page_num += 1

            # 手动发送请求
            yield scrapy.Request(url=new_url, callback=self.parse)


