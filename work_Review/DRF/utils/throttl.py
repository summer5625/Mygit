# -*- coding: utf-8 -*-
# @Time    : 2020/2/24  16:55
# @Author  : XiaTian
# @File    : throttl.py
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
import time


VISIT_RECORD = {}


class MyThrottle(SimpleRateThrottle):

    scope = 'WD'

    def get_cache_key(self, request, view):
        
        key = self.get_ident(request)
        
        return key

