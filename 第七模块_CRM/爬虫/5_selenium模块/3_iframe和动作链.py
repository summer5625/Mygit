# -*- coding: utf-8 -*-
# @Time    : 2019/12/6  16:38
# @Author  : XiaTian
# @File    : 3_iframe和动作链.py
import time
from selenium import webdriver
from selenium.webdriver import ActionChains  # 导入动作链


bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')


# 定位标签存在于iframe标签之中，不能直接定位到标签，需要通过如下操作，然后在进行标签定位
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

# 创建动作链
action = ActionChains(bro)

# 点击长按选中标签
action.click_and_hold(div)

# 拖动标签
for i in range(5):

    # move_by_offset(x,y),对应的是想x和y方向移动多少距离
    # perform()是让动作立即执行
    action.move_by_offset(17,0).perform()
    time.sleep(1)

# 释放动作链
action.release()

time.sleep(3)

bro.quit()