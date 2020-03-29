# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  17:19
# @Author  : XiaTian
# @File    : baidu_news_home.py
from framework.base_page import BasePage


class NewsHomePage(BasePage):

    sport_link = "xpath=>//*[@id='channle-all']/div/ul/li[7]/a"

    def click_sport(self):
        self.click(self.sport_link)
        self.sleep(2)