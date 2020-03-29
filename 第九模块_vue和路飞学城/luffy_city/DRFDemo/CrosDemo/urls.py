# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  22:10
# @Author  : XiaTian
# @File    : urls.py

from django.contrib import admin
from django.urls import path
from CrosDemo import views


urlpatterns = [
    path('test/', views.CorsView.as_view())
]