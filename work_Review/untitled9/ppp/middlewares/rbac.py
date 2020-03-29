# -*- coding: utf-8 -*-
# @Time    : 2020/2/6  19:38
# @Author  : XiaTian
# @File    : rbac.py
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.conf import settings


class RbacMiddlerware(MiddlewareMixin):

    def process_request(self, request):

        permission_list = request.session.get(settings.PERMISSION_KEY)
        current_url = request.path_info

        for url in settings.WHITE_LIST:
            
            reg = '^%s$' % url
            if re.match(reg, current_url):
                return None

        if not permission_list:
            return HttpResponse('未获取到用户权限，请登录!')

        record_url = [{'title': '首页', 'url': '#'}]
        flag = False
        
        for url in permission_list.values():

            reg = '^%s$' % url['url']
            
            if re.match(reg, current_url):
                flag = True
                request.current_check_pid = url['pid'] or url['id']
                if not url['pid']:
                    record_url.extend([{'title': url['title'], 'url': url['url']}])
                else:
                    record_url.extend([{'title': url['p_title'], 'url': url['p_url']},
                                       {'title': url['title'], 'url': url['url'], 'class': 'active'}])
                request.breadcrumb = record_url
                break

        if not flag:
            return HttpResponse('没有访问权限!')


















