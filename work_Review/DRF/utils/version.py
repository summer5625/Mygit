# -*- coding: utf-8 -*-
# @Time    : 2020/2/23  18:36
# @Author  : XiaTian
# @File    : version.py
from rest_framework import versioning


class MyVersion(object):

    def determine_version(self, request, *args, **kwargs):

        version = request.query_params.get('version', 'v1')

        return version