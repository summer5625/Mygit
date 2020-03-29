# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  22:58
# @Author  : XiaTian
# @File    : TestRunner.py
import unittest
from baidu_search import BaiduSearch
from test_get_page_title import GetPageTitle

# 执行多个不同文件中的测试脚本（一个个添加测试用例）
# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTitle('test_get_page_title'))

# 加载测试类中所有测试用例
suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)