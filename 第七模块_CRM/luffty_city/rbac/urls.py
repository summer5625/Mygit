# -*- coding: utf-8 -*-
# @Time    : 2019/10/26  19:09
# @Author  : XiaTian
# @File    : urls.py

from django.urls import path, re_path

from rbac.views import roles
from rbac.views import user
from rbac.views import menu


urlpatterns = [
    path('role/list/', roles.role_list, name = 'role_list'),
    path('role/add/', roles.role_add, name = 'role_add'),
    path('user/list/', user.user_list, name = 'user_list'),
    path('user/add/', user.user_add, name = 'user_add'),
    path('menu/list/', menu.menu_list, name = 'menu_list'),
    path('menu/add/', menu.menu_add, name = 'menu_add'),
    path('multi/permission/', menu.multi_permission, name = 'multi_permission'),
    path('distribute/permission/', menu.distribute_permission, name = 'distribute_permission'),


    re_path(r'^role/edit/(?P<pk>\d+)/$', roles.role_edit, name = 'role_edit'),
    re_path(r'^role/del/(?P<pk>\d+)/$', roles.role_del, name = 'role_del'),
    re_path(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name = 'user_edit'),
    re_path(r'^user/del/(?P<pk>\d+)/$', user.user_del, name = 'user_del'),
    re_path(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name = 'user_reset_pwd'),
    
    re_path(r'^menu/edit/(?P<pk>\d+)/$', menu.menu_edit, name = 'menu_edit'),
    re_path(r'^menu/del/(?P<pk>\d+)/$', menu.menu_del, name = 'menu_del'),

    re_path(r'^second/menu/edit/(?P<pk>\d+)/$', menu.second_menu_edit, name = 'second_menu_edit'),
    re_path(r'^second/menu/del/(?P<pk>\d+)/$', menu.second_menu_del, name = 'second_menu_del'),
    re_path(r'^second/menu/add/(?P<menu_id>\d+)$', menu.second_menu_add, name = 'second_menu_add'),
    
    re_path(r'^permission/add/(?P<second_menu_id>\d+)$', menu.permission_add, name = 'permission_add'),
    re_path(r'^permission/edit/(?P<pk>\d+)/$', menu.permission_edit, name = 'permission_edit'),
    re_path(r'^permission/del/(?P<pk>\d+)/$', menu.permission_del, name = 'permission_del'),
    re_path(r'^multi/permission/del/(?P<pk>\d+)/$', menu.multi_permission_del, name='multi_permission_del')
    
]