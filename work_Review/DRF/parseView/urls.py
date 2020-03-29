# -*- coding: utf-8 -*-
# @Time    : 2020/2/25  12:53
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from parseView.views import *


urlpatterns = [
    path('', ParserTest.as_view())
]