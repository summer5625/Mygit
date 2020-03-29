# -*- coding: utf-8 -*-
# @Time    : 2019/10/28  16:13
# @Author  : XiaTian
# @File    : urls.py

from django.urls import reverse
from django.http import QueryDict


def memory_url(request, name, *args, **kwargs):
    '''
    生成带有原搜索条件的url（替代模板中的url）
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    '''

    basic_url = reverse(name, args=args, kwargs=kwargs)

    # 如果用户没有提交搜索条件
    if not request.GET:

        return basic_url

    query_dict = QueryDict(mutable=True)
    query_dict['_filter'] = request.GET.urlencode()  # request.GET.urlencode()获取用户的搜索条件即地址？后面的一串字符串

    return '%s?%s' % (basic_url, query_dict.urlencode())


def memory_reverse(request, name, *args, **kwargs):
    '''
    反向生成urls，是将原来的搜索条件拼接到本次跳转的url中
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    '''

    url = reverse(name, args=args, kwargs=kwargs)
    origin_params = request.GET.get('_filter')

    if origin_params:
        url = '%s?%s' % (url, origin_params)
  
    return url