# -*- coding: utf-8 -*-
# @Time    : 2019/11/26  23:43
# @Author  : XiaTian
# @File    : urls.py

from django.contrib import admin
from django.urls import path
from authDemo import views

urlpatterns = [
    path('', views.AuthView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('test/', views.TestView.as_view()),
]
