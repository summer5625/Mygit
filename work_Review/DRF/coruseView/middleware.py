# -*- coding: utf-8 -*-
# @Time    : 2020/2/25  19:17
# @Author  : XiaTian
# @File    : middleware.py
from django.middleware.security import SecurityMiddleware
from django.utils.deprecation import MiddlewareMixin


class MyCourse(MiddlewareMixin):

    def process_response(self, request, reponse):

        reponse['Access-Control-Allow-Origin'] = '*'
        return reponse