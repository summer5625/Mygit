# -*- coding: utf-8 -*-
import scrapy
from boosPro.items import BoosproItem


class BoosSpider(scrapy.Spider):
    name = 'boos'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://www.lagou.com/zhaopin/Python/?labelWords=label']
    start_urls = ['https://www.lagou.com/zhaopin/Python/2/?filterOption=3&sid=7ed580c79dae4967aab434665ef7733b']
    url = 'https://www.lagou.com/zhaopin/Python/%s/?filterOption=2&sid=2020e026e1784ed9bdb286846ccdf30e'
    page_num = 2

    def parse_detail(self, response):

        item = response.meta['item']

        job_desc = response.xpath('//dl[@id="job_detail"]/dd[2]/div//text()').extract()
        job_desc = ''.join(job_desc)
        item['desc'] = job_desc

        yield item

    def parse(self, response):
        print(response)
        li_list = response.xpath('//*[@id="s_position_list"]/ul/li')

        for li in li_list:
            item = BoosproItem()
            job_name = li.xpath('./div[1]/div[1]/div[1]/a/h3/text()').extract_first()
            detail_url = li.xpath('./div[1]/div[1]/div[1]/a/@href').extract_first()
            item['job'] = job_name

            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        # if self.page_num <= 3:
        #     new_url = self.url % self.page_num
        #     self.page_num += 1
        #     # print(new_url)
        #
        #     yield scrapy.Request(url=new_url, callback=self.parse)


