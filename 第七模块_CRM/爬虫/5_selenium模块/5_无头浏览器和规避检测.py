# -*- coding: utf-8 -*-
# @Time    : 2019/12/6  17:01
# @Author  : XiaTian
# @File    : 5_无头浏览器和规避检测.py
from selenium import webdriver
from time import sleep

# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions


# 实现无可视化界面操作（固定操作，代码不变）
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测，固定格式
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 让selenium实现规避检测
bro = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options, options=option)

# 无可视化界面
bro.get('https://www.baidu.com/')

print(bro.page_source)
sleep(2)
bro.quit()