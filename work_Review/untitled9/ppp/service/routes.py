# -*- coding: utf-8 -*-
# @Time    : 2020/2/2  16:02
# @Author  : XiaTian
# @File    : routes.py
import re
from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import URLResolver, URLPattern


def check_url_exclude(url):
    
    for regex in settings.AUTO_DISCOVER_EXCLUDE:
        if re.match(regex, url):
            return True


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):

    for item in urlpatterns:  # 循环每一条url
        if isinstance(item, URLPattern):
            if not item.name: # url没有别名
                continue
    
            if pre_namespace: # 将路由分发上一级的名称空间和当前url的别名拼接
                name = '%s:%s' % (pre_namespace, item.name)
            else:
                name = item.name
    
            url = pre_url + str(item.pattern)
            url = url.replace('^', '').replace('$', '')  # 重新生成新的url
    
            if check_url_exclude(url):
                continue
            
            url_ordered_dict[name] = {'name': name, 'url': url}

        elif isinstance(item, URLResolver):  # 路由分发
            if pre_namespace:
                if item.namespace:
                    namespace = '%s:%s' % (pre_namespace, item.namespace)
                else:
                    namespace = item.namespace
            else:
                if item.namespace:
                    namespace = item.namespace
                else:
                    namespace = None
            recursion_urls(namespace, pre_url + str(item.pattern), item.url_patterns, url_ordered_dict)

        
def get_all_url_dict():

    url_ordered_dict = OrderedDict()
    md = import_string(settings.ROOT_URLCONF)
    recursion_urls(None, '/', md.urlpatterns, url_ordered_dict)

    return url_ordered_dict