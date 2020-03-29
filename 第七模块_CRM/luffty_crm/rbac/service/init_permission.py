# -*- coding: utf-8 -*-
# @Time    : 2019/10/25  11:20
# @Author  : XiaTian
# @File    : init_permission.py

from django.conf import settings


def init_permission(request, current_user):
    '''
    初始化用户权限
    :param request:
    :param current_user:
    :return:
    '''

    # 获取登录成功用户的权限
    permissions = current_user.roles.filter(
        permissions__isnull=False).values(
        'permissions__pid',  # 拥有权限的id
        'permissions__url',  # 拥有权限的url
        'permissions__title', # 拥有权限的名称
        'permissions__menu__title', # 一级菜单的名称
        'permissions__menu__icon',  # 一级菜单的图标
        'permissions__menu__mid',   # 一级菜单的id
        'permissions__p_id',        # 不能作为菜单的权限所属能作为菜单权限的id（父级菜单权限的id）
        'permissions__p_id__url',
        'permissions__p_id__title',
        'permissions__name').distinct()

    permission_list = {}
    menu_dict = {}

    for item in permissions:
        permission_list[item['permissions__name']] = {
                'id': item['permissions__pid'],
                'url': item['permissions__url'],
                'pid': item['permissions__p_id'],
                'title': item['permissions__title'],
                'p_title': item['permissions__p_id__title'],
                'p_url': item['permissions__p_id__url']}

        menu_id = item['permissions__menu__mid']
        if not menu_id:  # 不能作为菜单就进行下一个循环
            continue

        # 子菜单的信息
        node = {'id': item['permissions__pid'], 'title': item['permissions__title'], 'url': item['permissions__url']}
        if menu_id in menu_dict: # 添加到二级菜单列表

            menu_dict[menu_id]['children'].append(node)

        else:

            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'], # 父级菜单的标题
                'icon': item['permissions__menu__icon'],   # 父级菜单的图标
                'children': [node, ]
            }

    # 设置权限到session
    request.session[settings.PERMISSION_KEY] = permission_list
    request.session[settings.MENU_LIST_KEY] = menu_dict
