# -*- coding: utf-8 -*-
# @Time    : 2019/12/28  15:12
# @Author  : XiaTian
# @File    : 5_wait_time.py
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 打开Chrome浏览器
driver.get('https://www.baidu.com/')  # 打开百度
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()  # 点击【登录】；click() 方法，可模拟在按钮上的一次鼠标单击。
# B. 确定元素的定位表达式
ele_locator = "TANGRAM__PSP_10__footerULoginBtn"  # 通过id,确定‘用户名登录’元素

# C.  使用expected_conditions对应的方法来生成判断条件
# EC.方法名(定位方式,定位表达式)
# EC.visibility_of_element_located(By.ID,ele_locator)#元素可见

# D.  调用WebDriverWait类设置等待总时长、轮询周期
# WebDriverWait(driver, 超时时长, 调用频率（默认0.5s）).until(可执行方法, 超时时返回的信息)
# 等待10秒钟，每隔1秒去查看对应的元素是否可见；如果可见，继续下一步操作；如果不可见，则继续等待，直到10s结束，如果元素还是不可见，则抛出超时异常
WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.ID, ele_locator)))

driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()  # 点击【用户名登录】

driver.close()  # 关闭当前窗口