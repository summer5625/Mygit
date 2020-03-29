# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  17:19
# @Author  : XiaTian
# @File    : news_sport_home.py
from framework.base_page import BasePage


class SportNewsHomePage(BasePage):

    nba_link = "xpath=>//*[@id ='col_nba']/div[1]/div[2]/ul[1]/li[2]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)