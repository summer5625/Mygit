# -*- coding: utf-8 -*-
# @Time    : 2020/2/23  21:57
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from authView.views import *


urlpatterns = [
    path('', AuthDemo.as_view()),
    path('login/', Login.as_view()),
    path('test', TestVier.as_view())
]