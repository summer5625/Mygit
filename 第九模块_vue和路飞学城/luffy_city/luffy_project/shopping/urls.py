# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  15:49
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from shopping import views
from shopping import settlement_view
from shopping import payment

urlpatterns = [
    path('car/', views.ShoppingCarView.as_view()),
    path('settlement', settlement_view.SettlementView.as_view()),
    path('payment', payment.PaymentView.as_view()),
]
