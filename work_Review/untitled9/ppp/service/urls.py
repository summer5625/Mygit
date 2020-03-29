# -*- coding: utf-8 -*-
# @Time    : 2020/2/5  16:29
# @Author  : XiaTian
# @File    : urls.py
from django.urls import reverse
from django.http import QueryDict


def memory_url(request, name, *args, **kwargs):

    basic_url = reverse(name, args=args, kwargs=kwargs)

    if not request.GET:
        return basic_url
    query_dict = QueryDict(mutable=True)
    query_dict['_filter'] = request.GET.urlencode()
    return '%s?%s' % (basic_url, query_dict.urlencode())


def memory_reverse(request, name, *args, **kwargs):

    url = reverse(name, args=args, kwargs=kwargs)
    origin_params = request.GET.get('_filter')
    
    if origin_params:
        url = '%s?%s' % (url, origin_params)
    return url