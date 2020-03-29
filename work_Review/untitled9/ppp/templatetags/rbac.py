# -*- coding: utf-8 -*-
# @Time    : 2020/2/1  19:12
# @Author  : XiaTian
# @File    : rbac.py
from collections import OrderedDict
from django import template
from django.conf import settings
from ppp.service import urls


register = template.Library()


@register.inclusion_tag('static_menu.html')
def static_menu(request):
    
    menu_list = request.session[settings.MENU_LIST_KEY]
    
    return {'menu_list': menu_list}


@register.inclusion_tag('multi_menu.html')
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


@register.filter
def has_permission(request, name):

    if name in request.session[settings.PERMISSION_KEY]:
        return True


@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    
    return urls.memory_url(request, name, *args, **kwargs)




















