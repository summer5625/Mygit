# -*- coding: utf-8 -*-
# @Time    : 2019/11/3  12:48
# @Author  : XiaTian
# @File    : stark.py

from django.urls import path
from app01 import views

class StarkSite(object):

    def __init__(self):

        self._register = []

    def get_url(self):
        patterns = []

        for app in self._register:

            patterns.append(path('%s' % app, views.index))

        return patterns

    @property
    def urls(self):

        return (self.get_url(), None, None)


site = StarkSite()

