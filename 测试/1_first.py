# -*- coding: utf-8 -*-
# @Time    : 2019/12/27  14:33
# @Author  : XiaTian
# @File    : 1_first.py
from selenium import webdriver
import time


# bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# bro.get('https://www.baidu.com')
# time.sleep(2)
# bro.close()

bro = webdriver.Firefox(executable_path='./geckodriver.exe')

size = bro.get_window_size() # 获取窗口尺寸
print(size)
bro.maximize_window() # 窗口最大化
time.sleep(1)
bro.set_window_size(800, 600) # 设置窗口的自定义尺寸
time.sleep(1)
# bro.minimize_window() # 窗口最小化
bro.get('https://www.baidu.com')
# bro.get_screenshot_as_file('screen.png') # 获取网页截图
time.sleep(1)
bro.get('http://news.baidu.com/')
bro.back()
time.sleep(1)
bro.forward()
time.sleep(1)
bro.close()

