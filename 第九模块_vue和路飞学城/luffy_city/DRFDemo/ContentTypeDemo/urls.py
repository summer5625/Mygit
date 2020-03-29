# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  23:17
# @Author  : XiaTian
# @File    : urls.py

from django.contrib import admin
from django.urls import path
from ContentTypeDemo import views


urlpatterns = [
    path('test/', views.ContentTypeView.as_view())
]