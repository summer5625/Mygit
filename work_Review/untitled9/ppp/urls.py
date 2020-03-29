"""untitled9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from ppp.views import user
from ppp.views import role
from ppp.views import menu


urlpatterns = [
    path('user/list/', user.user_list, name='user_list'),
    path('user/add/', user.user_add, name='user_add'),
    re_path(r'user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
    re_path(r'user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
    re_path(r'user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name='user_reset_pwd'),
    
    path('role/list/', role.role_list, name='role_list'),
    path('role/add/', role.role_add, name='role_add'),
    re_path(r'^role/edit/(?P<pk>\d+)/$', role.role_edit, name='role_edit'),
    re_path(r'^role/del/(?P<pk>\d+)/$', role.role_del, name='role_del'),

    path('menu/list/', menu.menu_list, name='menu_list'),
    path('menu/add/', menu.menu_add, name='menu_add'),
    re_path(r'^menu/edit/(?P<pk>\d+)/$', menu.menu_edit, name='menu_edit'),
    re_path(r'^menu/del/(?P<pk>\d+)/$', menu.menu_del, name='menu_del'),

    re_path(r'^second/menu/add/(?P<menu_id>\d+)/$', menu.second_menu_add, name='second_menu_add'),
    re_path(r'^second/menu/edit/(?P<pk>\d+)/$', menu.second_menu_edit, name='second_menu_edit'),
    re_path(r'^second/menu/del/(?P<pk>\d+)/$', menu.second_menu_del, name='second_menu_del'),
    
    re_path(r'^permission/add/(?P<second_menu_id>\d+)/$', menu.permission_add, name='permission_add'),
    re_path(r'^permission/edit/(?P<pk>\d+)/$', menu.permission_edit, name='permission_edit'),
    re_path(r'^permission/del/(?P<pk>\d+)/$', menu.permission_del, name='permission_del'),

    path('multi/permission/', menu.multi_permission, name='multi_permission'),
    re_path(r'^multi/permission/del/(?P<pk>\d+)/$', menu.multi_permission_del, name='multi_permission_del'),
    path('distribute/permission/', menu.distribute_permission, name = 'distribute_permission'),
]
