# -*- coding: utf-8 -*-
# @Time    : 2019/12/30  0:33
# @Author  : XiaTian
# @File    : TestRunner2.py
import unittest


# 加载一个目录下的所有文件中的测试用例
suite = unittest.TestLoader().discover('testsuites')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)