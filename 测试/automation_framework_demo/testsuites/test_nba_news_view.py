# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  17:26
# @Author  : XiaTian
# @File    : test_nba_news_view.py
import time
import unittest
from framework.browswe_engine import BrowserEngine
from pageobjecys.baidu_home_page import HomePage
from pageobjecys.baidu_news_home import NewsHomePage
from pageobjecys.news_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.bro = browser.open_browser(self)

    def tearDown(self):
        self.bro.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.bro)
        # baiduhome.click_news()
        self.bro.find_element_by_xpath("//*[@id='u1']/a[@name='tj_trnews']").click()
        # 初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.bro)
        # newshome.click_sport()
        self.bro.find_element_by_xpath("//*[@id='channel-all']/div/ul/li[7]/a").click()
        # 初始化一个体育新闻主页，点击NBA
        soprtnewhome = SportNewsHomePage(self.bro)
        # soprtnewhome.click_nba_link()
        self.bro.find_element_by_xpath("//*[@id ='col_nba']/div[1]/div[2]/ul[1]/li[2]/a").click()
        soprtnewhome.get_window_img()


if __name__ == '__main__':
    unittest.main()




















