# -*- coding: utf-8 -*-
# @Time    : 2020/2/25  18:56
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from coruseView.views import *


urlpatterns = [
    path('test', Course.as_view())
]