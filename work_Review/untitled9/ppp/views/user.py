# -*- coding: utf-8 -*-
# @Time    : 2020/1/28  18:15
# @Author  : XiaTian
# @File    : user.py
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from ppp import models
from ppp.forms import user


def user_list(request):

    user_queryset = models.UserInfo.objects.all()
    
    return render(request, 'user_list.html', {'users': user_queryset})


def user_add(request):

    if request.method == 'GET':
        form = user.UserModelFrom()
        return render(request, 'change.html', {'form': form})

    form = user.UserModelFrom(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:user_list'))
    return render(request, 'change.html', {'form': form})


def user_edit(request, pk):

    user_obj = models.UserInfo.objects.filter(pk=pk).first()
    
    if not user_obj:
        return HttpResponse('用户不存在')
    
    if request.method == 'GET':
        form = user.UpdateUser(instance=user_obj)
        return render(request, 'change.html', {'form': form})
    
    form = user.UpdateUser(instance=user_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:user_list'))
    return render(request, 'change.html', {'form': form})


def user_del(request, pk):

    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': reverse('ppp:user_list')})
    models.UserInfo.objects.filter(pk=pk).delete()
    return redirect(reverse('ppp:user_list'))


def user_reset_pwd(request, pk):

    user_obj = models.UserInfo.objects.filter(pk=pk).first()

    if not user_obj:
        return HttpResponse('用户不存在')

    if request.method == 'GET':
        form = user.ResetPassword()
        return render(request, 'change.html', {'form': form})
    
    form = user.ResetPassword(instance=user_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:user_list'))

    return render(request, 'change.html', {'form': form})






















