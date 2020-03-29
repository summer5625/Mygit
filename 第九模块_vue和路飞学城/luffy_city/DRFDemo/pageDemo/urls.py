# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  16:39
# @Author  : XiaTian
# @File    : urls.py
from django.contrib import admin
from django.urls import path
from pageDemo import views


urlpatterns = [
    path('book/', views.BookView.as_view()),
]