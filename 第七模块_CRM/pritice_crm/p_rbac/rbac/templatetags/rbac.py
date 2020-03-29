# -*- coding: utf-8 -*-
# @Time    : 2019/11/16  14:29
# @Author  : XiaTian
# @File    : rbac.py

from collections import OrderedDict
from django import template
from django.conf import settings

from rbac.service import urls


register = template.Library()


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):

    menu_dict = request.session[settings.MENU_LIST_KEY]

    key_list = sorted(menu_dict)

    ordered_dict = OrderedDict()

    for key in key_list:

        val = menu_dict[key]
        val['class'] = 'hide'
        
        for per in val['children']:

            if per['id'] == request.current_check_pid:
                
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):

    return {'record_list': request.breadcrumb}


@register.filter
def has_permission(request, name):
    
    if name in request.session[settings.PERMISSION_KEY]:
        
        return True


@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    
    return urls.memory_url(request, name, *args, **kwargs)


    


















