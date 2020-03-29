# -*- coding: utf-8 -*-
# @Time    : 2019/11/15  14:27
# @Author  : XiaTian
# @File    : payment.py

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app01.forms import payment
from app01 import models


def payment_list(request):
    """
    付费列表
    :return:
    """
    data_list = models.Payment.objects.all()
    return render(request, 'payment_list.html', {'data_list': data_list})


def payment_add(request):
    """
    编辑付费记录
    :return:
    """
    if request.method == 'GET':
        form = payment.PaymentForm()
        return render(request, 'rbac/change.html', {'form': form})
    form = payment.PaymentForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request, 'rbac/change.html', {'form': form})


def payment_edit(request, pk):
    """
    新增付费记录
    :return:
    """
    obj = models.Payment.objects.get(pk=pk)
    if request.method == 'GET':
        form = payment.PaymentForm(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})
    form = payment.PaymentForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request, 'rbac/change.html', {'form': form})


def payment_del(request,pk):
    """
    删除付费记录
    :param request:
    :param pk:
    :return:
    """
    models.Payment.objects.filter(pk=pk).delete()
    return redirect('/payment/list/')
