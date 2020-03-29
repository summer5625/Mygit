# -*- coding: utf-8 -*-
# @Time    : 2019/12/27  16:15
# @Author  : XiaTian
# @File    : 3_assert.py
from selenium import webdriver
import time


dro = webdriver.Chrome(executable_path='./chromedriver.exe')
dro.get('https://baidu.com')
time.sleep(1)
dro.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(1)
dro.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
time.sleep(1)
# dro.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__memberPass"]').click()
# time.sleep(1)

try:
    dro.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__memberPass"]').is_selected()
    print('ok')

    time.sleep(2)

except Exception as e:
    print(e)
# try:
#     assert u"百度一下" in dro.title
#     print('assert ok')
#
# except Exception as e:
#     print(e)
#
dro.quit()