# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  22:40
# @Author  : XiaTian
# @File    : middlewares.py

from django.utils.deprecation import MiddlewareMixin


# 使用添加响应头的方式解决跨域
class MyCors(MiddlewareMixin):

    def process_response(self, request, response):

        response['Access-Control-Allow-Origin'] = '*' # *是代表告诉浏览器任何域都不拦截

        if request.method == 'OPTIONS':

            response['Access-Control-Allow-Methods'] = 'PUT,DELETE'
            response['Access-Control-Allow-Headers'] = 'content-type'

        return response
