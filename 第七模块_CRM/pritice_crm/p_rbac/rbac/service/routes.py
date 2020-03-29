# -*- coding: utf-8 -*-
# @Time    : 2019/11/15  19:19
# @Author  : XiaTian
# @File    : routes.py

import re
from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import URLResolver, URLPattern


def check_url_exclude(url):

    for item in settings.AUTO_DISCOVER_EXCLUDE:
        if re.match(item, url):
            return True
    

def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):

    for item in urlpatterns:
        
        if isinstance(item, URLPattern): # 不是路由分发

            # path('user/list/', user.user_list, name='user_list'),
            if not item.name: # url没有设置别名，则跳过该url
                continue
                 
            if pre_namespace:
                name = '%s:%s' % (pre_namespace, item.name) # 反向生成url时用
            else:
                name = item.name

            url = pre_url + str(item.pattern)
            url = url.replace('^', '').replace('$', '')

            if check_url_exclude(url):
                continue

            url_ordered_dict[name] = {'name': name, 'url': url}
        
        elif isinstance(item, URLResolver): # 是路由分发

            if pre_namespace:

                if item.namespace:
                    namespace = '%s:%s' % (pre_namespace, item.namespace)
                else:
                    namespace = pre_namespace
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


