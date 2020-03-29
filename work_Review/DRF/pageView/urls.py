# -*- coding: utf-8 -*-
# @Time    : 2020/2/24  20:33
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from pageView.views import *


urlpatterns = [
    path('', Book.as_view()),
]