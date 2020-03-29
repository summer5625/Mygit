# -*- coding: utf-8 -*-
# @Time    : 2019/9/27  0:16
# @Author  : XiaTian
# @File    : ulconvert.py


class MonthConvert:

    regex = '[0-9]{2}'  #regex这个名称不能为其他名称

    def to_python(self, value):

        print('to_python:', value)
        return int(value)

    #用于反向解析
    def to_url(self, value):

        print('to_url:', value)
        return '%04d' % value
