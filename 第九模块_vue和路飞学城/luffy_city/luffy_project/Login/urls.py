# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  14:25
# @Author  : XiaTian
# @File    : urls.py

from django.urls import path
from Login import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('test_auth', views.TestView.as_view()),
]