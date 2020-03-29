# -*- coding: utf-8 -*-
# @Time    : 2019/10/14  14:25
# @Author  : XiaTian
# @File    : my_middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect

from Middleware_model import settings


# 自定义中间件
# class CustomerMiddleware(MiddlewareMixin):
# 
# 
#     def process_request(self, request):
# 
#         print('CustomerMiddleware process_request....')
# 
# 
#     def process_response(self, request, response):
# 
#         print('CustomerMiddleware process_response.....')
# 
#         return response
# 
# 
#     def process_view(self, request, callback, callback_args, callback_kwargs):
# 
#         print('CustomerMiddleware process_view.....')
#         print('callback:', callback)
# 
# 
#     def process_exception(self, request, exception):
# 
#         print('CustomerMiddleware exception....')
# 
# 
# class CustomerMiddleware2(MiddlewareMixin):
# 
# 
#     def process_request(self, request):
# 
#         print('CustomerMiddleware2 process_request....')
# 
# 
#     def process_response(self, request, response):
# 
#         print('CustomerMiddleware2 process_response.....')
# 
#         return response
# 
# 
#     def process_view(self, request, callback, callback_args, callback_kwargs):
# 
#         print('CustomerMiddleware2 process_view.....')
#         print('callback:', callback)
# 
# 
#     def process_exception(self, request, exception):
# 
#         print('CustomerMiddleware2 exception....')
#         return HttpResponse(exception)


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        white_list = settings.WHITE_LIST
        if request.path not in white_list:

            if not request.user.is_authenticated:

                return redirect('/login/')
