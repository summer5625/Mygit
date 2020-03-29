# -*- coding: utf-8 -*-
# @Time    : 2019/10/25  15:10
# @Author  : XiaTian
# @File    : rbac.py


from collections import OrderedDict
from django import template


from luffty_city import settings
from rbac.service import urls


register = template.Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    '''
    一级菜单
    :param request:
    :return:
    '''

    menu_list = request.session[settings.MENU_LIST_KEY]

    return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    '''
    二级菜单
    :param request:
    :return:
    '''

    menu_dict = request.session[settings.MENU_LIST_KEY]

    # 对字典key值进行排序，确保用户每次打开页面时，菜单顺序都是固定的
    key_list = sorted(menu_dict)

    # 空的有序字典
    ordered_dict = OrderedDict()

    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'

        for per in val['children']:

            # reg = "^%s$" % per['url']
            
            if per['id'] == request.current_check_pid: # 判断用户提交路径是否符合权限，符合权限就显示二级菜单
                per['class'] = 'active'
                val['class'] = ''

        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}


@register.filter
def has_permission(request, name):
    '''
    判断是否有权限，自定义过滤器最多只能有两个参数,用于权限粒度控制
    :param request:
    :param name:
    :return:
    '''
    if name in request.session[settings.PERMISSION_KEY]:

        return True


@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    '''
    反向生成urls，是将原来的搜索条件拼接到本次跳转的url中
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    '''
    return urls.memory_url(request, name, *args, **kwargs)















