# -*- coding: utf-8 -*-
# @Time    : 2020/2/23  17:02
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from version.views import *


urlpatterns = [
    path('', DemoView.as_view()),
]
