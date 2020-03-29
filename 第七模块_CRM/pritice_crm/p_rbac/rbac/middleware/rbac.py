# -*- coding: utf-8 -*-
# @Time    : 2019/11/16  15:08
# @Author  : XiaTian
# @File    : rbac.py


import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.conf import settings


class RbacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        
        permission_dict = request.session.get(settings.PERMISSION_KEY)
        current_url = request.path_info

        for url in settings.WHITE_LIST:
            reg = '^%s$' % url

            if re.match(reg, current_url):
                return None

        record_url = [
            {'title': '首页', 'url': '#'},
        ]

        for i in settings.NO_PERMISSION_LIST:

            if re.match(i, current_url):
                request.current_check_pid = 0
                request.breadcrumb = record_url

                return None

        if not permission_dict:
            return HttpResponse('未获取到用户权限，请登录!')

        flag = False
        for url in permission_dict.values():

            reg = '^%s$' % url['url']

            if re.match(reg, current_url):
                flag = True
                request.current_check_pid = url['pid'] or url['id']
               
                if not url['pid']: 
                    record_url.extend([{'title': url['title'], 'url': url['url']}])

                else:
                    record_url.extend([
                        {'title': url['p_title'], 'url': url['p_url']},
                        {'title': url['title'], 'url': url['url'], 'class': 'active'}
                    ])
                request.breadcrumb = record_url
                break

        if not flag:

            return HttpResponse('没有访问权限!')















