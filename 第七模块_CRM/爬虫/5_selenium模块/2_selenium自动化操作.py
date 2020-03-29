# -*- coding: utf-8 -*-
# @Time    : 2019/12/6  15:48
# @Author  : XiaTian
# @File    : 2_selenium自动化操作.py
from selenium import webdriver
import time


bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://docs.qq.com/doc/DRUp1aUpSaWppYmtu')

time.sleep(5)
search_te = bro.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]//text()')
print(search_te)

# 标签定位
# search_input = bro.find_element_by_id('q')
#
# # 标签交互：向搜索框提交搜索内容
# search_input.send_keys('狗')
#
# # 执行js代码，拖动滚轮
# bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
#
# # 点击搜索按钮
# btn = bro.find_element_by_css_selector('.btn-search')
# btn.click()
#
# # 浏览器页面前进后退
# bro.get('https://www.baidu.com/')
# time.sleep(2)
#
# # 后退到上一个页面
# bro.back()
# time.sleep(2)
#
# # 前进到下一个页面
# bro.forward()
#
#
# time.sleep(5)
bro.quit()