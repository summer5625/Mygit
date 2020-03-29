# -*- coding: utf-8 -*-
# @Time    : 2019/11/26  22:34
# @Author  : XiaTian
# @File    : urls.py

from django.contrib import admin
from django.urls import path
from versionDemo import views


urlpatterns = [
    path('', views.DemoView.as_view())
]