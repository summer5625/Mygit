# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  17:26
# @Author  : XiaTian
# @File    : TestRunner_Report.py
import os
import time
import unittest
import HTMLTestRunner


report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/test_report/'
now = time.strftime('%m%d%H%M%S', time.localtime(time.time())) + '.html'
report_name = report_path + now
fp = open(report_name, 'w', encoding='utf-8')
case_path = os.path.join(os.getcwd(), '')
print(case_path)

# suite = unittest.TestLoader().discover(case_path, 'baidu_search.py', top_level_dir=None)

# 使用正则表达式匹配对应目录下的所有符合匹配规则的测试用例
suite = unittest.TestLoader().discover(case_path, 'test*.py', top_level_dir=None)

if __name__ == '__main__':

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例测试情况')
    runner.run(suite)
    fp.close()