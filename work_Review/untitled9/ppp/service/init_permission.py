# -*- coding: utf-8 -*-
# @Time    : 2020/2/6  13:48
# @Author  : XiaTian
# @File    : init_permission.py
from django.conf import settings


def init_permission(request, current_user):

    permissions = current_user.roles.filter(permissions__isnull=False).values(
        'permissions__id', 'permissions__url', 'permissions__title', 'permissions__menu__title',
        'permissions__menu__icon', 'permissions__menu__id', 'permissions__p_id', 'permissions__p_id__url',
        'permissions__p_id__title', 'permissions__name').distinct()

    permission_list = {}
    menu_dict = {}
   
    for item in permissions:
        permission_list[item['permissions__name']] = {
            'id': item['permissions__id'],
            'url': item['permissions__url'],
            'pid': item['permissions__p_id'],
            'title': item['permissions__title'],
            'p_title': item['permissions__p_id__title'],
            'p_url': item['permissions__p_id__url']
        }

        menu_id = item['permissions__menu__id']
        if not menu_id:
            continue

        node = {'id': item['permissions__id'], 'title': item['permissions__title'], 'url': item['permissions__url']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }

    request.session[settings.PERMISSION_KEY] = permission_list
    request.session[settings.MENU_LIST_KEY] = menu_dict

























