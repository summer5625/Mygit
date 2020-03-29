# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangPro.items import WangproItem


class WangSpider(scrapy.Spider):
    name = 'wang'

    start_urls = ['https://news.163.com/']
    model_urls = []

    # 初始化爬虫源文件
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r'D:\practice_Python_code\untitled\第七模块_CRM\爬虫\6_scrapy框架\wangPro\wangPro\spiders\chromedriver.exe')

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3, 4, 6, 7, 8]

        for li in alist:

            model_url = li_list[li].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)

        for url in self.model_urls:

            yield scrapy.Request(url=url, callback=self.parse_model)

    def parse_model(self, response):

        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')

        for div in div_list:
            item = WangproItem()
            title = div.xpath('./div/div[@class="news_title"/h3/a/text()]').extract_first()
            item['title'] = title
            new_detail_url = div.xpath('./a/@href').extract_first()

            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):

        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)

        item = response.meta['item']
        item['content'] = content

        yield item

    def closed(self, spider):

        self.bro.quit()