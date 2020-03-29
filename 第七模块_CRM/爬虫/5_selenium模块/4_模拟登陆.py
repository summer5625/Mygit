# -*- coding: utf-8 -*-
# @Time    : 2019/12/6  16:46
# @Author  : XiaTian
# @File    : 4_模拟登陆.py
import time
from selenium import webdriver


bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

username = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
btn = bro.find_element_by_id('login_button')

username.send_keys('458684403')
password.send_keys('xiayun5625')
btn.click()

time.sleep(3)

bro.quit()