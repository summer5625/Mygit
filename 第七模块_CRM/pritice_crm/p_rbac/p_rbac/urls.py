"""p_rbac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from app01.views import customer
from app01.views import payment
from app01.views import account


urlpatterns = [

    path('admin/', admin.site.urls),
    path('rbac/', include(('rbac.urls', 'rbac'))),
    path('login/', account.login),
    path('logout/', account.logout),
    path('index/', account.index),

    path('customer/list/', customer.customer_list, name='customer_list'),
    path('customer/add/', customer.customer_add, name='customer_add'),
    re_path(r'^customer/del/(?P<pk>\d+)/$', customer.customer_del, name='customer_del'),
    re_path(r'^customer/edit/(?P<pk>\d+)/$', customer.customer_edit, name='customer_edit'),
    re_path(r'^customer/import/$', customer.customer_import, name='customer_import'),
    re_path(r'^customer/tpl/$', customer.customer_tpl, name='customer_tpl'),
    
    path('payment/list/', payment.payment_list, name='payment_list'),
    path('payment/add/', payment.payment_add, name='payment_add'),
    re_path(r'^payment/del/(?P<pk>\d+)/$', payment.payment_del, name='payment_del'),
    re_path(r'^payment/edit/(?P<pk>\d+)/$', payment.payment_edit, name='payment_edit'),

]


