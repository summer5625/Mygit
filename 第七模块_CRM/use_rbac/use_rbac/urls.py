"""use_rbac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path, include


from app01.views import user
from app01.views import account
from app01.views import host
from app01.views import depart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rbac/', include(('rbac.urls', 'rbac'))),
    path('user/list/', user.user_list, name='user_list'),
    path('user/add/', user.user_add, name='user_add'),
    path('login/', account.login, name='login'),
    path('logout/', account.logout, name='logout'),
    path('index/', account.index, name='index'),
    path('host/list/', host.host_list, name='host_list'),
    path('host/add/', host.host_add, name='host_add'),
    path('depart/list/', depart.depart_list, name='depart_list'),
    path('depart/add/', depart.depart_add, name='depart_add'),

    re_path(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
    re_path(r'^user/del/(?P<pk>\d+)/$', user.user_del, name = 'user_del'),
    re_path(r'^user/reset/password/(?P<pk>\d+)/$', user.user_reset_pwd, name = 'user_reset_pwd'),
    re_path(r'^host/edit/(?P<pk>\d+)/$', host.host_edit, name = 'host_edit'),
    re_path(r'^host/del/(?P<pk>\d+)/$', host.host_del, name = 'host_del'),
    re_path(r'^depart/edit/(?P<pk>\d+)/$', depart.depart_edit, name = 'depart_edit'),
    re_path(r'^depart/del/(?P<pk>\d+)/$', depart.depart_del, name = 'depart_del'),
]
