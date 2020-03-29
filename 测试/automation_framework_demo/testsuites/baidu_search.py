# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  1:28
# @Author  : XiaTian
# @File    : baidu_search.py
import time
import unittest
from framework.browswe_engine import BrowserEngine
from pageobjecys.baidu_home_page import HomePage


# class BaiduSearch(unittest.TestCase):
#
#     def setUp(self):
#         bro = BrowserEngine(self)
#         self.bro = bro.open_browser(self)
#
#     def tearDown(self):
#         self.bro.quit()
#
#     def test_baidu_search(self):
#         self.bro.find_element_by_id('kw').send_keys('selenium')
#         time.sleep(1)
#         self.bro.find_element_by_id('su').click()
#         time.sleep(3)
#
#         try:
#             assert 'selenium' in self.bro.title
#             print('Test Pass')
#
#         except Exception as e:
#             print('Test Fail', format(e))


class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.bro = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.bro.quit()

    def test_baidu_search(self):
        homepage = HomePage(self.bro)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        print('title-->', self.bro.title)

        try:
            assert ('selenium' in HomePage.get_page_title(self))
            print('Test Pass')
        except Exception as e:
            print('Test Fail {0}'.format(e))

    def test_search2(self):
        homepage = HomePage(self.bro)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        print('title-->', self.bro.title)

        try:
            assert ('python' in HomePage.get_page_title(self))
            print('Test Pass')
        except Exception as e:
            print('Test Fail {0}'.format(e))


# if __name__ == '__main__':
#     unittest.main()


if __name__ == '__main__':
    unittest.main()
