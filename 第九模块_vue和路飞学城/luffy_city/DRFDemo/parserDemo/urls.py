# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  17:56
# @Author  : XiaTian
# @File    : urls.py

from django.contrib import admin
from django.urls import path
from parserDemo import views


urlpatterns = [
    path('demo/', views.DjangoView.as_view()),
    path('test/', views.DRFParserView.as_view()),
]