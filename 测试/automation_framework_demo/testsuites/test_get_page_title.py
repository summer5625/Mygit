# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  22:45
# @Author  : XiaTian
# @File    : test_get_page_title.py
import unittest
from framework.browswe_engine import BrowserEngine
from pageobjecys.baidu_home_page import HomePage


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        browser = BrowserEngine(cls)
        cls.bro = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.bro.quit()

    def test_get_page_title(self):
        homepage = HomePage(self.bro)
        print(homepage.get_page_title())