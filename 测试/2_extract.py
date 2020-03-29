# -*- coding: utf-8 -*-
# @Time    : 2019/12/27  15:28
# @Author  : XiaTian
# @File    : 2_extract.py
import re, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


dro = webdriver.Chrome('./chromedriver.exe')
dro.implicitly_wait(6)  # 设置等待时间，在等待时间内等待网页加载完成它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，
                        # 如果元素可以定位，则继续执行；如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到
dro.get('https://baidu.com')
try:
    btn = dro.find_element_by_link_text('新闻')
    btn.click()
    print(dro.current_url) # 获取当前页面的url
    print(dro.title) # 获取当前页面的标题
    # dro.back()
    dro.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') # # 触发ctrl + t 打开一个新窗口
    dro.find_element_by_id('kw').send_keys(Keys.CONTROL + 'a') # # 触发ctrl + t 打开一个新窗口
    time.sleep(1)
    dro.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
    # dro.find_element_by_id('kw').send_keys('selenium')
    time.sleep(2)
    # dro.find_element_by_id('kw').clear() # 清除输入框内容
    # dro.refresh() # 刷新页面
    # print(dro.capabilities)  # 获取浏览信息
    # print('find')

except Exception as e:
    print(e)

dro.quit()



