# -*- coding: utf-8 -*-
# @Time    : 2019/11/26  23:11
# @Author  : XiaTian
# @File    : version.py
from rest_framework import versioning


# 版本控制类
class MyVersion(object):

    def determine_version(self, request, *args, **kwargs):
        # 返回值 给了request.version
        # 返回了版本号
        # 假设将版本号携带在url的过滤条件中  xxx/?version=v1
        version = request.query_params.get('version', 'v1')

        return version