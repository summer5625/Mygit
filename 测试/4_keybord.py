# -*- coding: utf-8 -*-
# @Time    : 2019/12/27  16:55
# @Author  : XiaTian
# @File    : 4_keybord.py

# 键盘事件
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# bro = webdriver.Chrome('./chromedriver.exe')
# bro.get('https://baidu.com')

# 键盘事件
# ele = bro.find_element(By.ID, 'kw')
# ele.send_keys('selenium&python')
# time.sleep(1)
# ele.send_keys(Keys.BACK_SPACE)  # 利用backspace键删除一个字符
# time.sleep(1)
# ele.send_keys(Keys.SPACE) # 在字符后面加一个空格
# time.sleep(1)
# ele.send_keys('study')  # 在字符后面加字符
# time.sleep(1)
# ele.send_keys(Keys.ENTER) # 键盘按下回车键
# time.sleep(1)

# ele.send_keys(Keys.CONTROL, 'a')  # 全选输入框的中内容
# ele.send_keys(Keys.CONTROL, 'x')  # 剪切选中内容
# ele.send_keys(Keys.CONTROL, 'v')  # 粘贴内容
# ele.submit()  # 提交搜索
# time.sleep(1)
#
# bro.execute_script("window.alert('弹框啊');") # 执行js
# time.sleep(2)
# bro.switch_to_alert().accept() # 点击弹出里面的确定按钮
# bro.switch_to_alert().dismiss() # 点击弹出里面的x
# time.sleep(3)
# bro.quit()

# 窗口切换
# bro = webdriver.Chrome('./chromedriver.exe')
# bro.get('http://news.baidu.com/')
# link = bro.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a')
# page1 = link.text
# print(link.text)
# print('current:', bro.current_window_handle) # 当前窗口的句柄
# link.click()
# time.sleep(2)
# handles = bro.window_handles
# print(handles)  # 当前全部窗口的句柄
#
#
# for handle  in handles:
#
#     if handle != bro.current_window_handle:
#         print(handle)
#
#         bro.close()
#         bro.switch_to.window(handle)
#         page2 = bro.find_element_by_xpath(".//*[@id='title_area']/h1").text
#         print(page2)
#         try:
#             assert page2 in page1
#             print('ok')
#         except Exception as e:
#             print(e)


bro = webdriver.Chrome('./chromedriver.exe')
# bro.get('http://news.baidu.com/')
bro.get('http://www.baidu.com/')

# for image in bro.find_elements_by_tag_name('img'):  # 获取 所有的图片标签elements 不是element
#
#     print(image.text, image.size, image.tag_name)

for link in bro.find_elements_by_xpath("//*[@href]"):

    print(link.get_attribute('href'))

bro.quit()















