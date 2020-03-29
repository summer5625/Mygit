# -*- coding: utf-8 -*-
# @Time    : 2019/10/29  21:19
# @Author  : XiaTian
# @File    : routes.py

import re
from collections import OrderedDict
from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import URLResolver, URLPattern


def check_url_exclude(url):
    """
    排除一些特定的URL
    :param url:
    :return:
    """
    for regex in settings.AUTO_DISCOVER_EXCLUDE:
        if re.match(regex, url):
            return True


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    '''
    递归的去循环获取项目中的url，是将有路由分发的url进行递归，直到没有路由分发为止
    :param pre_namespace: 分发路由时设置的名称空间
    :param pre_url: url前缀，用于拼接url(可以理解为父级的url)
    :param urlpatterns: url列表
    :param url_ordered_dict: 用于保存递归中获取的所有路由
    :return: 
    '''
    for item in urlpatterns:

        # 判断当前的url是不是路由分发，即path('rbac/', include(('rbac.urls', 'rbac')))
        if isinstance(item, URLPattern):
            
            if not item.name: # 判断当前的url有没有设置别名，没有设置别名就忽略
                continue
                
            if pre_namespace: # 当前url有名称空间，将其别名和父级名称空间拼接
                name = '%s:%s' % (pre_namespace, item.name)
            else: # 没有名称空间，name直接就是自己的url别名
                name = item.name

            url = pre_url + str(item.pattern) # 将父级的url和当前的url拼接,item.pattern获取的url不是一个字符串，要转换成字符串
            url = url.replace('^', '').replace  ('$', '') # 去掉正则匹配时的首位

            if check_url_exclude(url):
                continue
            
            url_ordered_dict[name] = {'name': name, 'url': url} # 将萍姐好的url别名和完整的url放到有序字典中

        # 当前url是路由分发路径
        elif isinstance(item, URLResolver):

            if pre_namespace: # 当前url有父级名称空间
                if item.namespace: # 当前url有自己的名称空间，将其名称空间和父级的名称空间拼接，作为下次递归的url的父级名称空间
                    namespace = '%s:%s' % (pre_namespace, item.namespace)
                else: # 当前url没有名称空间，下次递归的名称空间就是父级的名称空间
                    namespace = item.namespace

            else: # 当前url没有父级名称空间
                if item.namespace: # 当前url有自己的名称空间，下次递归的名称空间就是自己的名称空间
                    namespace = item.namespace
                else:
                    namespace = None

            recursion_urls(namespace, pre_url + str(item.pattern), item.url_patterns, url_ordered_dict)


def get_all_url_dict():
    '''
    获取项目中所有的URL（必须有name别名）
    :return:
    '''
    
    url_ordered_dict = OrderedDict()
    md =import_string(settings.ROOT_URLCONF)
    recursion_urls(None, '/', md.urlpatterns, url_ordered_dict)
    
    return url_ordered_dict





            
