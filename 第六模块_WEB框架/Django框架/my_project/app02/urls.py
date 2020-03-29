# -*- coding: utf-8 -*-
# @Time    : 2019/9/26  17:08
# @Author  : XiaTian
# @File    : urls.py

"""my_project URL Configuration

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
from django.urls import path, re_path #先引入re_path，相当用正则法则去匹配路径


from app02 import views


#路由配置就是用户请求的URL与views.py中函数的映射表。通过urls.py找到对应的函数
urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('^index1/$',views.index1),
    re_path('^index/$', views.index, name='index')

]
