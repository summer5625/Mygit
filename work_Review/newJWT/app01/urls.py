# -*- coding: utf-8 -*-
# @Time    : 2020/3/5  14:08
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token),
]