# -*- coding: utf-8 -*-
# @Time    : 2019/12/6  15:35
# @Author  : XiaTian
# @File    : 1_selenium基本使用.py
from selenium import webdriver
from lxml import etree
import time


# 实例化一个浏览器对象
bro = webdriver.Chrome(executable_path='chromedriver.exe')

# 让浏览器发送一个指定url对应请求
bro.get('http://125.35.6.84:81/xk/')

# 获取当前页面的所有源码数据
page_text = bro.page_source

# 解析数据
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')

for li in li_list:

    title = li.xpath('./dl/@title')[0]
    print(title)

time.sleep(3)
bro.quit()